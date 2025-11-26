# Desmond-to-AMBER Trajectory Converter  
Convert open-source **Desmond** trajectories into **AMBER-compatible MDCRD** format for downstream analysis, including **MMPBSA.py**, CPPTRAJ, and related AMBER tools.

---

## Background

The **open-source Desmond MD package** developed by **D. E. Shaw Research (DESRES)** generates trajectory data in proprietary CMS/TRJ formats.  
Although these formats work seamlessly with the Desmond analysis tools, they are **not directly compatible** with:

- AMBER’s **MMPBSA.py**  
- **CPPTRAJ / PyTraj**  
- GROMACS/AMBER post-processing workflows  
- Free energy and decomposition tools that expect **AMBER-style coordinates**

Because of this incompatibility, anyone wishing to perform **MM-PBSA**, binding energy analysis, clustering, RMSD, PCA, hydrogen-bond analysis, etc., must **first convert the Desmond trajectory into a standard AMBER-readable file**.

This script solves that problem.


## What This Script Does

This Python script:

Reads a Desmond `.cms` file and associated trajectory frames  
Uses **open-source Desmond Python APIs only**  
Extracts physical atoms and maps internal indices correctly  
Builds a full coordinate series for all frames  
Writes a clean, AMBER-compatible **MDCRD** file  
Preserves correct atom ordering suitable for MMPBSA calculations  

Output:

