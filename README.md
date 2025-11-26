# Desmond → AMBER Trajectory Converter  
Convert Desmond `.cms` trajectory files to AMBER `mdcrd` format.

This script uses Schrödinger Desmond's internal Python API to load a CMS model and trajectory frames and then exports the coordinates as an AMBER-compatible MDCRD file.

---

## 📦 Requirements

You must run this script **inside a Schrödinger environment** (tested on 2020-1):

```bash
$SCHRODINGER/run python trj_convert.py
