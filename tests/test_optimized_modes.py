"""Independent CLI checks for the optimized square-lattice enumerator.

The expected values come from the archived A001411 data and the Python
reference enumerator.  These tests exercise the executable as a black box;
they do not inspect its bitset or memo-table representation.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest

from src.reference_enumerator import counts


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "optimized_enumerator.cpp"
DATA = ROOT / "data" / "A001411.txt"


def _oeis_counts() -> list[int]:
    values: dict[int, int] = {}
    for line in DATA.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        n, value = line.split()
        values[int(n)] = int(value)
    return [values[n] for n in range(max(values) + 1)]


@pytest.fixture(scope="module")
def optimized_binary(tmp_path_factory: pytest.TempPathFactory) -> Path:
    compiler = shutil.which("g++")
    if compiler is None:
        pytest.skip("g++ unavailable")
    directory = tmp_path_factory.mktemp("optimized-enumerator")
    executable = directory / "saw_enum"
    subprocess.run(
        [compiler, "-std=c++20", "-O2", "-DNDEBUG", str(SOURCE), "-o", str(executable)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return executable


def _run(executable: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(executable), *arguments],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize("mode", [(), ("--memo-small",)], ids=["default", "memo-small"])
@pytest.mark.parametrize("max_n", [10, 12])
def test_both_modes_match_reference_and_oeis(
    optimized_binary: Path, mode: tuple[str, ...], max_n: int
):
    completed = _run(optimized_binary, "--json", *mode, str(max_n))
    assert completed.returncode == 0, completed.stderr

    observed = json.loads(completed.stdout)
    expected = _oeis_counts()[: max_n + 1]
    assert observed == expected
    assert observed == counts(max_n)


def test_memo_small_rejects_length_above_cap(optimized_binary: Path):
    completed = _run(optimized_binary, "--json", "--memo-small", "13")

    assert completed.returncode != 0
    assert completed.stdout == ""
    assert "capped" in completed.stderr.lower()


def test_default_mode_rejects_length_above_proven_safety_cap(optimized_binary: Path):
    completed = _run(optimized_binary, "--json", "81")

    assert completed.returncode != 0
    assert completed.stdout == ""
    assert "safety cap" in completed.stderr.lower()


def test_memo_small_under_address_and_undefined_sanitizers(
    tmp_path: Path, optimized_binary: Path
):
    del optimized_binary  # The sanitizer build uses its own instrumented binary.
    compiler = shutil.which("g++")
    if compiler is None:
        pytest.skip("g++ unavailable")

    executable = tmp_path / "saw_enum_sanitized"
    compile_result = subprocess.run(
        [
            compiler,
            "-std=c++20",
            "-O1",
            "-g",
            "-fsanitize=address,undefined",
            "-fno-omit-frame-pointer",
            str(SOURCE),
            "-o",
            str(executable),
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if compile_result.returncode != 0:
        pytest.skip(f"sanitizer build unavailable: {compile_result.stderr}")

    environment = os.environ.copy()
    environment["ASAN_OPTIONS"] = "detect_leaks=0:halt_on_error=1"
    environment["UBSAN_OPTIONS"] = "halt_on_error=1:print_stacktrace=1"
    completed = subprocess.run(
        [str(executable), "--json", "--memo-small", "8"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )

    assert completed.returncode == 0, completed.stderr
    assert json.loads(completed.stdout) == _oeis_counts()[:9]
    assert completed.stderr == ""
