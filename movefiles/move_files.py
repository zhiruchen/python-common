import subprocess
import sys
from os import listdir
from os.path import isfile, join


def move_html_files(path, suffix, target_path):
    onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.endswith(suffix)]

    print("files count: ", len(onlyfiles))
    for file in onlyfiles:
        subprocess.run(["mv", file, target_path])

    print("all fiels move to", target_path)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3:
        print("args not enough")
    else:
        path, suffix, target_path = args[0], args[1], args[2]
        print('path: {path}, suffix: {suffix}, target_path: {target_path}'.\
            format(path=path, suffix=suffix, target_path=target_path))
        move_html_files(path, suffix, target_path)
