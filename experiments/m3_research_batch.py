"""Frozen-source receipts for the bounded M3 research batch; not M3 acceptance."""
import argparse
from src.provenance import run_record


def run(kind, run_id):
    common = ['experiments/m3_research_batch.py', 'src/provenance.py']
    if kind == 'span':
        from experiments.m3_span_probe import run as producer
        sources = ['experiments/m3_span_probe.py', 'src/bridge_spans.py',
                   'proofs/M3_SPAN_STRUCTURE_NOTES.md', 'NORMALIZATION.md']
        params = {'max_n': 30, 'weighted_max_n': 18, 'max_seconds': 60}
    elif kind == 'weights':
        from experiments.m3_weight_partition_probe import produce as producer
        sources = ['experiments/m3_weight_partition_probe.py', 'src/discovery_memory.py',
                   'src/equitable.py']
        params = {'memories': [3, 5, 7, 9, 11, 12]}
    elif kind == 'prudent':
        from proofs.m3_prudent_intervals import produce as interval_producer
        from proofs.m3_prudent_reference import counts
        def producer():
            return {'interval_certificate': interval_producer(), 'independent_geometry': counts()}
        sources = ['proofs/m3_prudent_intervals.py', 'proofs/m3_prudent_reference.py',
                   'papers/bacher-beaton-2014.pdf', 'references/bacher-beaton-2014.txt']
        params = {'bits': 384, 'root_brackets': 5, 'geometric_max_n': 12}
    elif kind == 'deadline':
        from experiments.m3_deadline_probe import probe_case
        def producer():
            return {'cases': [probe_case(m, max_states=100000, max_seconds=60,
                                         iterations=60, compare_raw=m <= 9)
                              for m in range(1, 14)]}
        sources = ['experiments/m3_deadline_probe.py', 'proofs/M3_AUTOMATON_SCOUT.md']
        params = {'memories': list(range(1, 14)), 'compare_raw_through': 9,
                  'max_states': 100000, 'case_seconds': 60, 'iterations': 60}
    else:
        raise ValueError(kind)
    return run_record(run_id,
                      f'PYTHONPATH=. .venv/bin/python experiments/m3_research_batch.py {kind} --run-id {run_id}',
                      params, common+sources, producer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=['span', 'weights', 'prudent', 'deadline'])
    parser.add_argument('--run-id', required=True)
    args = parser.parse_args()
    print(run(args.kind, args.run_id))
