// Exact square-lattice SAW enumerator.
//
// Build:
//   g++ -std=c++20 -O3 -DNDEBUG src/optimized_enumerator.cpp -o saw_enum
// Run:
//   ./saw_enum 14
//   ./saw_enum --json 14
//
// The first step is fixed to +x and the resulting counts are multiplied by
// four.  This is valid because the root is at the origin and the four first
// steps are related by square-lattice rotations; all orientations remain in
// the reported count.  Counts use unsigned __int128.  The executable accepts
// n <= 80, for which the non-backtracking bound
//   c_n <= 4 * 3^(n-1) <= 197078439219127897754777613608511063468
// is strictly below 2^128-1.  Thus every increment and the final factor four
// are proven not to overflow (the useful benchmark range is n <= 20).

#include <algorithm>
#include <array>
#include <charconv>
#include <cstddef>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <system_error>
#include <unordered_map>
#include <vector>

namespace saw {

using count_type = unsigned __int128;
constexpr std::size_t MAX_SAFE_N = 80;
constexpr std::size_t MAX_MEMO_N = 12;

class Enumerator {
public:
    explicit Enumerator(std::size_t max_n, bool use_memo)
        : max_n_(max_n), side_(checked_side(max_n)), origin_(max_n + 1),
          visited_(checked_words(side_), 0), use_memo_(use_memo) {
        if (use_memo_ && max_n_ > MAX_MEMO_N) {
            throw std::invalid_argument(
                "--memo is capped at max_n <= 12");
        }
        if (use_memo_) {
            path_.reserve(max_n_ + 1);
        }
    }

    std::vector<count_type> run() {
        std::vector<count_type> counts(max_n_ + 1);
        counts[0] = 1;
        if (max_n_ == 0) {
            return counts;
        }

        // Every walk of length at most max_n stays in the square bounded by
        // [-max_n, max_n]^2.  The extra one-cell border makes every neighbor
        // check below a simple array-bound check.
        const std::size_t root = index(origin_, origin_);
        const std::size_t first = index(origin_ + 1, origin_);
        set_visited(root, true);
        set_visited(first, true);
        if (use_memo_) {
            path_.push_back({origin_, origin_});
            path_.push_back({origin_ + 1, origin_});
            const auto& continuation = memoized_continuations(
                origin_ + 1, origin_, max_n_ - 1);
            for (std::size_t extra = 0; extra < continuation.size(); ++extra) {
                counts[extra + 1] = continuation[extra];
            }
            path_.clear();
        } else {
            counts[1] = 1; // the single +x-rooted walk of length one
            visit(origin_ + 1, origin_, 1, counts);
        }
        set_visited(first, false);
        set_visited(root, false);

        for (std::size_t n = 1; n <= max_n_; ++n) {
            counts[n] *= 4;
        }
        return counts;
    }

private:
    struct Point {
        std::size_t x;
        std::size_t y;
    };

    struct RelativeVertex {
        int x;
        int y;

        bool operator==(const RelativeVertex&) const = default;

        bool operator<(const RelativeVertex& other) const {
            return x < other.x || (x == other.x && y < other.y);
        }
    };

    struct MemoKey {
        std::size_t remaining;
        std::vector<RelativeVertex> occupied;

        bool operator==(const MemoKey&) const = default;
    };

    struct MemoKeyHash {
        std::size_t operator()(const MemoKey& key) const noexcept {
            std::size_t hash = std::hash<std::size_t>{}(key.remaining);
            for (const RelativeVertex vertex : key.occupied) {
                const auto x = static_cast<std::uint32_t>(vertex.x);
                const auto y = static_cast<std::uint32_t>(vertex.y);
                const auto packed = (static_cast<std::uint64_t>(x) << 32) | y;
                const std::size_t mixed = std::hash<std::uint64_t>{}(packed);
                hash ^= mixed + static_cast<std::size_t>(0x9e3779b97f4a7c15ULL) +
                        (hash << 6) + (hash >> 2);
            }
            return hash;
        }
    };

    static std::size_t checked_side(std::size_t max_n) {
        const std::size_t limit = std::numeric_limits<std::size_t>::max();
        if (max_n > (limit - 3) / 2) {
            throw std::invalid_argument("max_n is too large for the visited array");
        }
        return 2 * max_n + 3;
    }

    static std::size_t checked_area(std::size_t side) {
        const std::size_t limit = std::numeric_limits<std::size_t>::max();
        if (side != 0 && side > limit / side) {
            throw std::invalid_argument("max_n is too large for the visited array");
        }
        return side * side;
    }

    static std::size_t checked_words(std::size_t side) {
        const std::size_t area = checked_area(side);
        const std::size_t limit = std::numeric_limits<std::size_t>::max();
        if (area > limit - 63) {
            throw std::invalid_argument("visited bitset is too large");
        }
        return (area + 63) / 64;
    }

    std::size_t index(std::size_t x, std::size_t y) const {
        return y * side_ + x;
    }

    bool is_visited(std::size_t cell) const {
        const std::size_t word = cell >> 6;
        const std::size_t bit = cell & 63;
        return (visited_[word] & (std::uint64_t{1} << bit)) != 0;
    }

    void set_visited(std::size_t cell, bool value) {
        const std::size_t word = cell >> 6;
        const std::size_t bit = cell & 63;
        const std::uint64_t mask = std::uint64_t{1} << bit;
        if (value) {
            visited_[word] |= mask;
        } else {
            visited_[word] &= ~mask;
        }
    }

    void visit(std::size_t x, std::size_t y, std::size_t depth,
               std::vector<count_type>& counts) {
        if (depth == max_n_) {
            return;
        }

        // Keeping the four directions explicit avoids signed coordinate
        // arithmetic at the array boundary and makes the safety invariant
        // apparent: only in-range, unvisited vertices are marked.
        try_step(x + 1, y, depth, counts);
        try_step(x, y + 1, depth, counts);
        if (x > 0) {
            try_step(x - 1, y, depth, counts);
        }
        if (y > 0) {
            try_step(x, y - 1, depth, counts);
        }
    }

    void try_step(std::size_t x, std::size_t y, std::size_t depth,
                  std::vector<count_type>& counts) {
        if (x >= side_ || y >= side_) {
            return;
        }
        const std::size_t cell = index(x, y);
        if (is_visited(cell)) {
            return;
        }
        set_visited(cell, true);
        ++counts[depth + 1];
        visit(x, y, depth + 1, counts);
        set_visited(cell, false);
    }

    static RelativeVertex transform(RelativeVertex vertex,
                                     std::size_t symmetry) {
        switch (symmetry) {
        case 0:
            return {vertex.x, vertex.y};
        case 1:
            return {vertex.x, -vertex.y};
        case 2:
            return {-vertex.x, vertex.y};
        case 3:
            return {-vertex.x, -vertex.y};
        case 4:
            return {vertex.y, vertex.x};
        case 5:
            return {vertex.y, -vertex.x};
        case 6:
            return {-vertex.y, vertex.x};
        default:
            return {-vertex.y, -vertex.x};
        }
    }

    MemoKey canonical_key(std::size_t endpoint_x, std::size_t endpoint_y,
                          std::size_t remaining) const {
        std::vector<RelativeVertex> canonical;
        canonical.reserve(path_.size());
        for (std::size_t symmetry = 0; symmetry < 8; ++symmetry) {
            std::vector<RelativeVertex> candidate;
            candidate.reserve(path_.size());
            for (const Point point : path_) {
                const RelativeVertex relative{
                    static_cast<int>(point.x) - static_cast<int>(endpoint_x),
                    static_cast<int>(point.y) - static_cast<int>(endpoint_y)};
                candidate.push_back(transform(relative, symmetry));
            }
            std::sort(candidate.begin(), candidate.end());
            if (symmetry == 0 || candidate < canonical) {
                canonical = std::move(candidate);
            }
        }
        return {remaining, std::move(canonical)};
    }

    const std::vector<count_type>& memoized_continuations(
        std::size_t x, std::size_t y, std::size_t remaining) {
        MemoKey key = canonical_key(x, y, remaining);
        const auto found = memo_.find(key);
        if (found != memo_.end()) {
            return found->second;
        }

        std::vector<count_type> result(remaining + 1);
        result[0] = 1;
        if (remaining != 0) {
            memo_try_step(x + 1, y, remaining, result);
            memo_try_step(x, y + 1, remaining, result);
            if (x > 0) {
                memo_try_step(x - 1, y, remaining, result);
            }
            if (y > 0) {
                memo_try_step(x, y - 1, remaining, result);
            }
        }

        auto inserted = memo_.emplace(std::move(key), std::move(result));
        return inserted.first->second;
    }

    void memo_try_step(std::size_t x, std::size_t y,
                       std::size_t remaining,
                       std::vector<count_type>& result) {
        if (x >= side_ || y >= side_) {
            return;
        }
        const std::size_t cell = index(x, y);
        if (is_visited(cell)) {
            return;
        }
        set_visited(cell, true);
        path_.push_back({x, y});
        const auto& child = memoized_continuations(x, y, remaining - 1);
        for (std::size_t extra = 0; extra < child.size(); ++extra) {
            result[extra + 1] += child[extra];
        }
        path_.pop_back();
        set_visited(cell, false);
    }

    std::size_t max_n_;
    std::size_t side_;
    std::size_t origin_;
    std::vector<std::uint64_t> visited_;
    bool use_memo_;
    std::vector<Point> path_;
    std::unordered_map<MemoKey, std::vector<count_type>, MemoKeyHash> memo_;
};

std::vector<count_type> counts(std::size_t max_n, bool use_memo = false) {
    if (max_n > MAX_SAFE_N) {
        throw std::invalid_argument(
            "max_n exceeds the proven unsigned __int128 safety cap (80)");
    }
    if (use_memo && max_n > MAX_MEMO_N) {
        throw std::invalid_argument("--memo is capped at max_n <= 12");
    }
    return Enumerator(max_n, use_memo).run();
}

} // namespace saw

namespace {

struct Options {
    bool json = false;
    bool memo = false;
    std::size_t max_n = 0;
};

std::size_t parse_max_n(const std::string& text) {
    if (text.empty() || text.front() == '-') {
        throw std::invalid_argument("max_n must be a nonnegative integer");
    }
    std::size_t value = 0;
    const char* begin = text.data();
    const char* end = begin + text.size();
    const auto parsed = std::from_chars(begin, end, value);
    if (parsed.ec == std::errc::result_out_of_range || parsed.ptr != end) {
        throw std::invalid_argument("max_n must be a nonnegative integer");
    }
    return value;
}

Options parse_options(int argc, char** argv) {
    if (argc < 2) {
        throw std::invalid_argument(
            "usage: optimized_enumerator [--json] [--memo|--memo-small] MAX_N");
    }
    Options options;
    bool have_max_n = false;
    for (int i = 1; i < argc; ++i) {
        const std::string argument(argv[i]);
        if (argument == "--json") {
            options.json = true;
        } else if (argument == "--memo" || argument == "--memo-small") {
            options.memo = true;
        } else if (argument == "-n" || argument == "--max-n") {
            if (i + 1 >= argc) {
                throw std::invalid_argument("missing value after --max-n");
            }
            if (have_max_n) {
                throw std::invalid_argument("max_n specified more than once");
            }
            options.max_n = parse_max_n(argv[++i]);
            have_max_n = true;
        } else if (argument.rfind("--max-n=", 0) == 0) {
            if (have_max_n) {
                throw std::invalid_argument("max_n specified more than once");
            }
            options.max_n = parse_max_n(argument.substr(8));
            have_max_n = true;
        } else if (!argument.empty() && argument.front() != '-') {
            if (have_max_n) {
                throw std::invalid_argument("max_n specified more than once");
            }
            options.max_n = parse_max_n(argument);
            have_max_n = true;
        } else if (argument == "--help" || argument == "-h") {
            std::cout << "usage: optimized_enumerator [--json] [--memo|--memo-small] MAX_N\n";
            std::cout << "       optimized_enumerator [--json] [--memo|--memo-small] --max-n MAX_N\n";
            std::exit(0);
        } else {
            throw std::invalid_argument("unknown option: " + argument);
        }
    }
    if (!have_max_n) {
        throw std::invalid_argument("missing max_n");
    }
    return options;
}

std::string decimal(saw::count_type value) {
    if (value == 0) {
        return "0";
    }
    std::string result;
    while (value != 0) {
        result.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

void print_counts(const std::vector<saw::count_type>& values, bool json) {
    if (json) {
        std::cout << '[';
        for (std::size_t n = 0; n < values.size(); ++n) {
            if (n != 0) {
                std::cout << ',';
            }
            std::cout << decimal(values[n]);
        }
        std::cout << "]\n";
        return;
    }
    for (std::size_t n = 0; n < values.size(); ++n) {
        std::cout << n << ' ' << decimal(values[n]) << '\n';
    }
}

} // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_options(argc, argv);
        print_counts(saw::counts(options.max_n, options.memo), options.json);
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
