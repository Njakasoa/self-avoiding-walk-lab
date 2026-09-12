"""Verify the immutable files in a published source snapshot (standard library)."""
from pathlib import Path
import hashlib
import json


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root/'SOURCE_MANIFEST.json').read_text())
    for rel, wanted in manifest['sha256'].items():
        path = (root/rel).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise RuntimeError(f'Missing or invalid snapshot file: {rel}')
        if hashlib.sha256(path.read_bytes()).hexdigest() != wanted:
            raise RuntimeError(f'Snapshot hash mismatch: {rel}')
    print(f"PASS: {len(manifest['sha256'])} snapshot files match SHA-256")


if __name__ == '__main__':
    main()
