#!/usr/bin/env python3
"""
Generate .ftp-deploy-sync-state.json from a local directory.

This tells SamKirkland/FTP-Deploy-Action that all current files
are already on the server, so only future changes get uploaded.

Usage:
    python generate_ftp_state.py [directory]
    python generate_ftp_state.py site/public

The state file is written to [directory]/.ftp-deploy-sync-state.json

This script is called by the GitHub Actions workflow after Hugo builds
but before the FTP Deploy Action runs. On the first run, it pre-seeds
the state file so the FTP action thinks everything is already synced.
On subsequent runs, the FTP action manages the state file itself.
"""
import hashlib
import json
import os
import sys
import time


def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def scan_directory(base_dir):
    data = []
    folders_seen = set()

    for root, dirs, files in sorted(os.walk(base_dir)):
        rel_root = os.path.relpath(root, base_dir)
        if rel_root == '.':
            rel_root = ''

        if rel_root:
            parts = rel_root.split(os.sep)
            for i in range(len(parts)):
                folder_path = '/'.join(parts[:i + 1])
                if folder_path not in folders_seen:
                    folders_seen.add(folder_path)
                    data.append({"type": "folder", "name": folder_path})

        for filename in sorted(files):
            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, base_dir).replace(os.sep, '/')

            # Skip the state file itself if it exists from a previous run
            if rel_path == '.ftp-deploy-sync-state.json':
                continue

            file_size = os.path.getsize(filepath)
            file_hash = sha256_file(filepath)

            data.append({
                "type": "file",
                "name": rel_path,
                "size": file_size,
                "hash": file_hash
            })

    return data


def main():
    base_dir = sys.argv[1] if len(sys.argv) > 1 else "site/public"

    if not os.path.isdir(base_dir):
        print(f"Error: {base_dir} is not a directory")
        sys.exit(1)

    print(f"Scanning {base_dir} for FTP state file generation...")
    data = scan_directory(base_dir)

    state = {
        "description": "DO NOT DELETE THIS FILE. This file is used to keep track of which files have been synced in the most recent deployment. If you delete this file a resync will need to be done (which can take a while) - read more: https://github.com/SamKirkland/FTP-Deploy-Action",
        "version": "1.0.0",
        "generatedTime": int(time.time() * 1000),
        "data": data
    }

    output_path = os.path.join(base_dir, ".ftp-deploy-sync-state.json")
    with open(output_path, 'w') as f:
        json.dump(state, f)

    folders = sum(1 for d in data if d['type'] == 'folder')
    files = sum(1 for d in data if d['type'] == 'file')
    size_mb = os.path.getsize(output_path) / (1024 * 1024)

    print(f"State file generated: {output_path}")
    print(f"  Folders: {folders}")
    print(f"  Files: {files}")
    print(f"  State file size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
