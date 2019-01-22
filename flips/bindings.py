"""
usage:
   flips [--apply] [--exact] patch.bps rom.smc [outrom.smc]
"""

import os
import subprocess

BASE_PATH = os.path.abspath(__file__)
FLIPS_PATH = os.path.join(BASE_PATH, 'flips')  # Path to Flips CLI binary


def _flips_command(args):
    stdout, stderr = subprocess.Popen([FLIPS_PATH] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if stderr.strip():
        print(f"flips stderr:\n{stderr}")

    return stdout


def apply_patch(patch_path, rom_path, output_path=None):
    args = ['--apply', patch_path, rom_path]
    if output_path is not None:
        args += output_path

    return _flips_command(args)
