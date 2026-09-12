"""Source-frozen receipts for the W proof and its finite falsification sweep."""
import argparse

from src.provenance import run_record


COMMON = [
    "experiments/w_research_batch.py", "src/provenance.py",
    "requirements-lock.txt", "proofs/W_NON_DFINITE.md",
    "proofs/W_DIRECTED_RAMPS.md", "proofs/M3_NON_DFINITE_CANDIDATE.md",
    "publication/main.tex", "papers/bacher-beaton-2014.pdf",
]


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: the interval engine requires assertions")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("identities", "critical", "phase", "phase-fine"))
    parser.add_argument("experiment_id")
    args = parser.parse_args()
    sources = list(COMMON)
    if args.kind == "identities":
        from experiments.w_exact_identities import produce as quotients
        from experiments.w_directed_ramps_check import produce as directed
        sources += ["experiments/w_exact_identities.py",
                    "experiments/w_directed_ramps_check.py"]
        parameters = {"directed_recurrence_max_k": 7, "numeric_dps": 70}

        def producer():
            return {"quotients": quotients(), "directed": directed()}
    elif args.kind == "critical":
        from proofs.w_critical_certificate import produce
        sources += ["proofs/w_critical_certificate.py",
                    "proofs/m3_critical_integrals.py", "proofs/m3_prudent_intervals.py"]
        parameters = {"bins": 2048, "power_bits": 16, "interval_bits": 384}

        def producer():
            return produce(bins=2048, power_bits=16)
    else:
        from experiments.w_phase_probe import run
        sources += ["experiments/w_phase_probe.py"]
        parameters = {"indices": [8, 16, 32, 64],
                      "phases": ["0.75", "0.80", "0.85", "0.87", "0.90"],
                      "dps": 90, "max_seconds": 180.0}
        if args.kind == "phase-fine":
            parameters.update(indices=[32, 64],
                              phases=["0.84", "0.85", "0.86", "0.87", "0.88", "0.89", "0.90"])

        def producer():
            result = run(**parameters)
            # Wall time belongs in metadata, not the deterministic payload.
            result.pop("runtime_seconds")
            return result
    command = f".venv/bin/python -m experiments.w_research_batch {args.kind} {args.experiment_id}"
    print(run_record(args.experiment_id, command, parameters, sources, producer))


if __name__ == "__main__":
    main()
