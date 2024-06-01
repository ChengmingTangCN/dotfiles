#!/bin/python3

import os
import sys
import subprocess


def check(**kwargs):
    if os.path.exists(kwargs["dest_path"]):
        print("{} already exists, please remote it and try again.".format(
            kwargs["dest_path"]))
        sys.exit(1)


def symlink(**kwargs):
    os.symlink(src=kwargs["resource_path"], dst=kwargs["dest_path"])


def is_program_installed(program_name):
    return subprocess.run(["which", program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0


if __name__ == "__main__":
    if not is_program_installed("nodejs"):
        print("nodejs is not installed, please install it and try again.")
    else:
        print("nodejs is installed")

    home_dir = os.path.expanduser("~")
    map_paths = [".vim", ".vimrc"]

    def do_map(fn):
        for map_path in map_paths:
            dest_path = os.path.abspath(os.path.join(home_dir, map_path))
            resource_path = os.path.abspath(map_path)
            fn(dest_path=dest_path, resource_path=resource_path)

    do_map(check)

    do_map(symlink)

    print("Setup successfully")
