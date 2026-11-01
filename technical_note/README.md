# Editable three-page Research Technical Note

This public source includes minimal frozen aggregate data, original plots and TikZ diagrams. It excludes raw trajectories, weights and private source archives.

Requirements: Python 3, Matplotlib 3.10.1, pdfTeX with Latin Modern, TikZ, standalone and the packages listed in `main.tex`, and Poppler `pdfinfo`.

Run `python -B build.py` in this directory. The three-page PDF is `build/main.pdf`; standalone diagram PDFs are also placed in `build/`. The script only plots saved aggregates and compiles documents. It does not call a model, refit a predictor or rerun a bootstrap. Fixed metadata and `SOURCE_DATE_EPOCH` support reproducible bytes within the documented environment; cross-platform TeX/font versions can change bytes.

Figure 1 separates recorded signals from derived evidence and predictions. Figure 2 uses four spacious panels to preserve all seven executed operations. Figure 3 contains four frozen paired comparisons. Figure 4 is proposed future work, not completed research. Availability is a separate quantitative panel on page 2.

The public repository supports aggregate/figure inspection, not independent raw-data reanalysis. See the repository publication-scope statement for exclusions and licensing limits.
