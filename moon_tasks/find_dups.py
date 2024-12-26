import typing as t
import os
import hashlib
from datetime import datetime


def hash_file(filename) -> str:
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        while chunk := file.read(8192):
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(folder: str, now: str) -> t.Tuple[t.Dict[str, str], t.Dict[str, str]]:
    hashes = {}
    dups = {}
    errors = []
    for dirpath, _, filenames in os.walk(folder):
        try:
            for f in filenames:
                full_path = os.path.join(dirpath, f)
                file_hash = hash_file(full_path)
                if file_hash in hashes:
                    dups[file_hash] = [full_path, hashes[file_hash]]
                # print(f"Duplicate found: {full_path} == {hashes[file_hash]}")
                else:
                    hashes[file_hash] = full_path
        except Exception as e:
            errors.append(e)
    
    with open(f'/tgldev/v{now}_errors.txt', 'w') as f:
        for e in errors:
            f.write(f"{e}\n")
    return dups, hashes


# find_duplicates('/path/to/your/folder')

if __name__ == '__main__':
    utcnow = datetime.utcnow()
    now = datetime.strftime(utcnow, '%Y%m%dT%H%M%S')
    print(f"Starting at {now}")
    SOURCE_DIR = '/home/'

    dups, files = find_duplicates(SOURCE_DIR, now=now)

    with open(f'/tgldev/v{now}_duplicates.txt', 'w') as f:
        for k, v in dups.items():
            f.write(f"{k} == {v}\n")

    with open(f'/tgldev/v{now}_files.txt', 'w') as f:
        for k, v in files.items():
            f.write(f"{k} == {v}\n")

