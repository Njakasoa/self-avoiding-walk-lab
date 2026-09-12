"""Create a public source snapshot from a committed lab revision, without history.

The destination must be empty. This never pushes or changes the source repo.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]


def exclusion(rel):
    path = Path(rel)
    if path.parts[0] in {'.agents', '.codex', 'memory', 'environment'}:
        return 'local operational notes, settings or original task material'
    if rel in {'AGENTS.md', 'ENVIRONMENT_AUDIT.md', 'ORCHESTRATION_LOG.md'}:
        return 'local operational instructions or machine audit'
    if path.parts[0] == 'papers' and path.suffix in {'.pdf', '.txt'}:
        return 'third-party paper; see references for original URL'
    if path.parts[0] == 'references' and path.suffix == '.txt':
        return 'third-party extracted full text'
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    dest = args.output.resolve()
    if dest.exists() and any(dest.iterdir()):
        raise RuntimeError('Destination must be empty; existing export preserved')
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    archive = subprocess.check_output(['git', 'archive', '--format=tar', revision], cwd=ROOT)
    excluded = {}
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(archive)) as source:
        for item in source:
            if item.isdir():
                continue
            rel = item.name
            if not item.isfile() or not (dest/rel).resolve().is_relative_to(dest):
                raise RuntimeError(f'Unexpected archive entry: {rel}')
            reason = exclusion(rel)
            if reason:
                excluded[rel] = reason
                continue
            target = dest/rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.extractfile(item).read())
    (dest/'README.md').write_bytes((dest/'publication/GITHUB_README.md').read_bytes())
    with (dest/'.gitignore').open('a') as out:
        out.write('\n# Local-only material omitted from the public snapshot\n')
        out.write('.agents/\n.codex/\nmemory/\nenvironment/\npapers/*.pdf\nreferences/*.txt\n')
    (dest/'papers').mkdir(exist_ok=True)
    (dest/'papers/README.md').write_text(
        '# Source papers\n\nThird-party PDFs and extracted full texts are not redistributed. '
        'See [data sources](../references/DATA_SOURCES.md), '
        '[the priority audit](../references/M3_NON_DFINITE_PRIORITY.md) and '
        '[the bibliography](../publication/references.bib) for original links.\n'
    )
    hashes = {str(p.relative_to(dest)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(dest.rglob('*')) if p.is_file()
              and str(p.relative_to(dest)) != 'publication/VALIDATION.json'}
    manifest = {'schema': 1, 'source_revision': revision,
                'repository': 'https://github.com/Njakasoa/self-avoiding-walk-lab',
                'history': 'curated snapshot; original lab commits are not included',
                'mutable_outputs_excluded': ['publication/VALIDATION.json'],
                'excluded_source_files': excluded, 'sha256': hashes}
    (dest/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'output': str(dest), 'files': len(hashes),
                      'excluded': len(excluded), 'source_revision': revision}, indent=2))


if __name__ == '__main__':
    main()
