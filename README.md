# QCL Filtering Project

This repository contains a **sample project** demonstrating filtering and analysis of **quantum cascade laser (QCL)** data. It was inspired by my research internship at **Princeton University**, where I worked on improving design processes for QCLs using machine learning and data analysis techniques.

**Note**: This project is a **simplified demonstration** and does not replicate the full extent of my Princeton research. Many essential datasets, design parameters, and computational tools used during the internship are unavailable due to licensing and confidentiality restrictions. As such, this project focuses on illustrating the filtering and visualization techniques applied in a general QCL context, using publicly available sample data.

---

## Project Overview

**Quantum cascade lasers (QCLs)** are advanced semiconductor lasers used in applications such as:
- Infrared spectroscopy
- Chemical sensing
- Optical communication

During my Princeton internship, I developed techniques to filter, analyze, and optimize QCL designs. This project demonstrates:
- Filtering QCL design data based on user-defined thresholds for key metrics.
- Visualizing filtered data distributions to aid in decision-making.

---

## What This Project Includes

This repository showcases:
1. **Filtering Techniques**:
   - Filters data based on thresholds for key parameters:
     - Electric Field (kV/cm)
     - Scattering Time (t_ul in ps)
     - Dipole Moment (z in Å)
     - Gain (g in cm/kA)
     - Figure of Merit (fom* in eV ps A²)
     - Energy Difference (Ediff in meV)

2. **Visualization**:
   - Histograms to visualize the distributions of key metrics after filtering.

3. **Customizable Parameters**:
   - Modify filtering thresholds directly in the script for tailored analyses.

---

## What This Project Does **Not** Include

While this repository demonstrates core filtering techniques, it does **not** represent the full scope of my Princeton research. Key differences include:
- **Dataset Limitations**:
  - The actual datasets used at Princeton, containing high-fidelity QCL design data, are not publicly available.
  - This project uses **publicly available sample data** sourced from [Princeton University Data Commons](https://datacommons.princeton.edu/discovery/catalog/doi-10-34770-r7nr-ee50).

- **Computational Models**:
  - The project does not include the **machine learning models** or simulation tools developed during my internship.

- **Depth of Analysis**:
  - The internship involved advanced optimization techniques and multi-parameter simulations that cannot be replicated with the current dataset.

As a result, this project serves as an **introductory demonstration** of the techniques and concepts, rather than a full replication of the work.

---

## Sample Data

This repository uses **publicly available QCL-related data** to replicate the basic filtering process. The data is sourced from [Princeton University Data Commons](https://datacommons.princeton.edu/discovery/catalog/doi-10-34770-r7nr-ee50). For more information about the dataset, visit the linked catalog page.

---

## Citation

If you use this project or the included sample data, please cite the following:

> Princeton University Data Commons. (2022). "QCL Simulation Dataset." DOI: [10.34770/r7nr-ee50](https://datacommons.princeton.edu/discovery/catalog/doi-10-34770-r7nr-ee50).

---
