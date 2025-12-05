# QSPS — Quantum Structure of the Perinuclear Space

This repository contains the LaTeX manuscript and reproducible code for the project

> **“Quantum structure of the perinuclear space and spectral invariants of the Coulomb field in hydrogen-like atoms.”**

The goal of the project is to analyse the radial potential and probability density in hydrogen–like atoms, to visualise the perinuclear region, and to study spectral invariants of the Coulomb field.

---

## Repository structure

```text
QSPS/
  README.md
  CITATION.cff
  LICENSE

  paper/
    main.tex          # LaTeX source of the preprint
    main.pdf          # compiled version of the paper
    figures/
      radial_density.png
      3d_density.png

  code/
    requirements.txt  # Python dependencies
    radial_density.py # scripts for 1D radial density plots
    density_3d.py     # scripts for 3D probability density visualisation
    utils.py          # shared numerical helpers (if needed)

  data/               # optional numerical data (if used)
```

---

## Requirements

* Python ≥ 3.10
* `pip` and virtual environments (`venv`)
* A working LaTeX distribution (e.g. TeX Live 2025 / MacTeX 2025)

Python packages are listed in `code/requirements.txt` (typical contents: `numpy`, `scipy`, `matplotlib`).

---

## Quick start: reproduce the figures

```bash
git clone https://github.com/cryptoinsider1/QSPS.git
cd QSPS

python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate

pip install -r code/requirements.txt
```

### Radial probability density

```bash
python code/radial_density.py
```

Output: `paper/figures/radial_density.png`.

### 3D probability density

```bash
python code/density_3d.py
```

Output: `paper/figures/3d_density.png`.

Adjust numerical parameters (principal quantum number `n`, orbital quantum number `l`, nuclear charge `Z`) directly in the scripts to explore different hydrogen-like systems.

---

## Building the LaTeX manuscript

```bash
cd paper
pdflatex main.tex
pdflatex main.tex    # run twice to resolve references
```

Resulting file: `main.pdf`.

---

## Citation

If you use this work, please cite the preprint and the repository.

> **Preprint**
> Vladimir Goncharov, *Quantum structure of the perinuclear space and spectral invariants of the Coulomb field in hydrogen-like atoms*, 2025.
> DOI: *to be assigned*
> arXiv: *to be assigned*.

A BibTeX template (update the DOI / arXiv IDs when available):

```bibtex
@article{Goncharov_QSPS_2025,
  author  = {Vladimir Goncharov},
  title   = {Quantum structure of the perinuclear space and spectral invariants of the Coulomb field in hydrogen-like atoms},
  year    = {2025},
  journal = {Preprint},
  note    = {Preprint, code and materials available at https://github.com/cryptoinsider1/QSPS},
  doi     = {10.0000/qsps.2025.00001},     % replace with real DOI
  eprint  = {arXiv:0000.00000},           % replace with real arXiv ID
}
```

---

## License

* Source code in `code/` is released under the **MIT License** (see `LICENSE`).
* The manuscript `paper/main.tex`, `paper/main.pdf` and figures in `paper/figures/` are licensed under **CC BY 4.0**.
