#!/bin/python3

import os
import sys
import subprocess


def check(**kwargs):
    if os.path.exists(kwargs["dest_path"]):
        print("{} already exists, please remove it and try again.".format(
            kwargs["dest_path"]))
        sys.exit(1)


def symlink(**kwargs):
    os.symlink(src=kwargs["resource_path"], dst=kwargs["dest_path"])


def is_program_installed(program_name):
    return subprocess.run(["which", program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0


if __name__ == "__main__":
    if not is_program_installed("alacritty"):
        print("alacritty is not installed, please install it and try again.")
        sys.exit(1)

    home_dir = os.path.expanduser("~")
    script_dir = os.path.dirname(os.path.realpath(__file__))

    def do_map(fn):
        dest_path = os.path.abspath(os.path.join(home_dir, ".config/alacritty"))
        resource_path = os.path.abspath(os.path.join(script_dir, "alacritty"))
        fn(dest_path=dest_path, resource_path=resource_path)

    do_map(check)

    do_map(symlink)

    print("Setup successfully")
