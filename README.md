# Desmond-to-AMBER Trajectory Converter

Convert open-source **Desmond** trajectories into **AMBER-compatible MDCRD** format for downstream analysis, including **MMPBSA.py**, CPPTRAJ, and related AMBER tools.

---

## Background

The **open-source Desmond MD package** developed by **D. E. Shaw Research (DESRES)** generates trajectory data in proprietary CMS/TRJ formats. Although these formats work seamlessly with the Desmond analysis tools, they are **not directly compatible** with:

- AMBER **MMPBSA.py**
- **CPPTRAJ / PyTraj**
- GROMACS/AMBER post-processing workflows
- Free energy and decomposition tools that expect **AMBER-style coordinates**

This script helps convert those trajectories into AMBER-readable output.

---

## What This Script Does

This Python script:

- Reads a Desmond `.cms` file and associated trajectory frames
- Uses Desmond Python APIs
- Extracts physical atoms and maps indices correctly
- Builds a full coordinate series for all frames
- Writes an **AMBER-compatible MDCRD** file
- Preserves atom ordering suitable for MMPBSA calculations

**Output example:**

`amber_trj.mdcrd`

---

## General Usage

```bash
/path/to/schrodinger/run python3 trj_convert.py -i /path/to/input.cms -o /path/to/output_prefix
```

### Parameters

- `-i` : Input Desmond CMS file
- `-o` : Output file prefix/name

---

## Example (Linux / WSL)

```bash
/opt/schrodinger2020-1/run python3 trj_convert.py -i desmond_md_job_1-out.cms -o amber_output
```

---

## Example (Any Installed Version)

```bash
$SCHRODINGER/run python3 trj_convert.py -i system-out.cms -o amber_output
```

---

## Notes

- Run the command from the folder containing your trajectory files.
- Keep `.cms` and trajectory frame folders/files together.
- Output can be used with AMBER tools after conversion.

