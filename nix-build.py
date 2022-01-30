#!/usr/bin/env python3
#
# A little wrapper around nix-build for terraform. The first argument is a
# JSON of args, attributes and path to build. And it outputs a JSON that
# contains the map of attribute to out path.
#

import json
import subprocess
import sys

def nix_build(args, attributes, path):
    cmd = ['nix-build', '--no-out-link', path] + args

    # Add all the attributes to build in order
    for attr in attributes:
        cmd.extend(["--attr", attr])

    # Run nix-build
    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        # check = True,
        encoding = 'utf-8',
        #env = { "NIX_PATH": "" }
    )
    stdout, stderr = process.communicate()

    # Get the outPaths, one per line. Those are ordered by the order of the
    # attributes.
    outPaths = stdout.splitlines()

    # Map back the out paths to the attributes
    return {attr: outPaths[i] for i, attr in enumerate(attributes)}

# Main

json.dump(
    nix_build(**json.loads(sys.argv[1])),
    sys.stdout,
    indent = 2,
)
