# Results and limitations

The exact unrounded values are in `public_data/aggregate_results.json`; CSV duplicates the 18 view/scope rows.

| View | Registered log loss | Full-tail log loss | Registered Brier | Full-tail Brier |
|---|---:|---:|---:|---:|
| Development prior | 0.1449 | 0.1449 | 0.0314 | 0.0314 |
| State + format | 0.1064 | 0.1064 | 0.0289 | 0.0289 |
| Ordinary replay | 0.0947 | 0.0947 | 0.0272 | 0.0272 |
| Likelihood proxy | 0.1152 | 0.1028 | 0.0296 | 0.0283 |
| State + replay + likelihood | 0.1054 | 0.0920 | 0.0282 | 0.0266 |
| Two-sample disagreement | 0.1040 | 0.0901 | 0.0282 | 0.0268 |
| Replay + task / deadlock | 0.0395 | 0.0429 | 0.0097 | 0.0113 |
| Task-relevance candidate | 0.0395 | 0.0429 | 0.0096 | 0.0112 |
| Matched generic interactions | 0.0402 | 0.0459 | 0.0103 | 0.0131 |

Lower is better. Four paired candidate-versus-baseline intervals cross zero. Tiny point gains do not resolve incremental value. This is not proof of equivalence or that better forecasts cannot help.

The primary calibration fit is unavailable because 30/30 at-risk calibration cases fail. Primary probabilities are uncalibrated. All-episode sensitivity has two successes among 32 calibration cases and is not a substitute.

Current-state availability is 61/224 (explicit grids or entity coordinates). All 25/224 available next-state forecasts are explicit full grids; only 1/224 is exact. No missing forecast is filled using simulator truth.

## Remaining uncertainty

- One small frozen model, symbolic fully observed deterministic Sokoban and fixed budget restrict generalization.
- Four final successes trigger the low-event warning; forecast sparsity limits informative error variation.
- Family grouping does not establish unseen-wall or training-data disjointness.
- Equal column counts and a common L2 penalty do not establish equal effective capacity; equal recorded spend is not optimal adaptive resource allocation.
- Finite likelihood proxies can reflect formatting and are not mutual information.
- Observed response dependence and correctness do not identify causal faithfulness.
- The inference interface was adapted during qualification; historical dataset generator identity and the RAGEN leaf commit remain unverified.
- Public aggregates allow inspection and rendering, not independent raw-data reanalysis.

Problem value, novelty, feasibility and evidence must remain separate: the question is concrete, the bounded implementation ran, the incremental comparison is inconclusive, and algorithmic novelty is not established (B: empirical finding). Forecast-rich, outcome-diverse follow-up evaluation is proposed only.
