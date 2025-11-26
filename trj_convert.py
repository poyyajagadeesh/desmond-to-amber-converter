#!/usr/bin/env python3

import argparse
import numpy as np

from schrodinger.application.desmond.packages import topo
from schrodinger.application.desmond.packages import traj
from schrodinger.application.desmond.packages import traj_util


def write_mdcrd(filename, coords_list):
    with open(filename, "w") as f:
        for coords in coords_list:
            flat = coords.reshape(-1, 3)
            for xyz in flat:
                f.write(f"{xyz[0]:8.3f}{xyz[1]:8.3f}{xyz[2]:8.3f}")
            f.write("\n")


def convert_to_amber(cms_path, output):
    print(f"Reading CMS: {cms_path}")

    msys_model, cms_model, tr = traj_util.read_cms_and_traj(cms_path)

    print(f"Trajectory frames: {len(tr)}")
    print(f"Atoms per frame (GIDs): {tr[0].natoms}")

    # ----------------------------------------------------------
    # FINAL WORKING METHOD FOR Desmond 2020-1:
    # msys_model.atoms → list of MSYS atom objects
    # Atom attributes vary in old versions → detect automatically
    # ----------------------------------------------------------
    msys_atoms = msys_model.atoms

    aids = []
    for atom in msys_atoms:
        if hasattr(atom, "atom_index"):
            aids.append(atom.atom_index)
        elif hasattr(atom, "index"):
            aids.append(atom.index + 1)  # make 1-based
        elif hasattr(atom, "id"):
            aids.append(atom.id + 1)     # make 1-based
        else:
            raise ValueError("Unknown MSYS Atom API: cannot find index attribute")

    print(f"Physical atoms detected: {len(aids)}")

    # Convert physical AIDs → GIDs
    gids = topo.aids2gids(cms_model, aids, include_pseudoatoms=False)

    print("Extracting coordinates...")

    coords_list = []
    for fr in tr:
        coords = fr.pos(gids)
        coords_list.append(coords)

    mdcrd = f"{output}.mdcrd"
    print(f"Writing MDCRD → {mdcrd}")
    write_mdcrd(mdcrd, coords_list)

    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", required=True, help="Input CMS file")
    parser.add_argument("-o", required=True, help="Output base name")
    args = parser.parse_args()

    convert_to_amber(args.i, args.o)
