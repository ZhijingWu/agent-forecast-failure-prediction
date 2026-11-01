# Experimental design

The model identifier, immutable checkpoint revision, pinned upstream SPA commit and frozen settings are in `public_data/experiment_config.json`. Parameter count (1,543,301,120) is the retained unique-parameter audit, not an inferred count from the model-page display.

## Execution and landmark

Native one-box 6 x 6 Sokoban permits ten attempted actions and five model turns. Temperature 0.7, top-p 0.8, top-k 20, maximum 400 new tokens per response. The prediction landmark follows the first proposed batch and returned native observation; zero mapped actions are possible. Failure is absence of native success within the fixed horizon. Already complete, terminal or out-of-budget cases are excluded from the primary landmark risk set.

## Shared packet and fixed views

Every view is charged the same recorded first response, extra initial sample, replay/task diagnostics and scores. Shared format/action/budget/output-length controls accompany the nonprior views. The task candidate adds nine forecast/task summaries to the 25-column replay/task baseline; matched generic interactions add nine other terms. View columns are listed verbatim in the aggregate feature register. This public register describes membership; it does not supply an executable trajectory feature extractor.

## Split and fit

| | Development | Calibration | Final |
|---|---:|---:|---:|
| Saved boards | 64 | 32 | 128 |
| D4 wall-plus-target families | 50 | 27 | 106 |
| At risk | 63 | 30 | 124 |
| At-risk successes / failures | 2 / 61 | 0 / 30 | 4 / 120 |

No family crosses splits. This does not prove unseen-wall or pretraining-disjoint generalization. StandardScaler and L2 logistic regression (C=1) use development labels only. Final data are not used to select features or tune settings. The 124 final at-risk episodes span 102 families.

## Likelihood scopes and uncertainty

Registered scope scores actual generated token IDs through the first closing think tag; this may mostly reflect formatting. Full-tail sensitivity scores the complete actual first-response tail under the same own/three-reference scheme. It adds 896 teacher-forcing passes and zero new samples. The full-tail plan was recorded after collection began but before analysis; it is not described as a wholly preregistered experiment.

Both scopes are finite length-normalized proxies, not exact mutual information or full RAGEN-2 reproductions. Each paired gain interval uses 2,000 wall-plus-target-family percentile resamples and conditions on the development fit; full retraining uncertainty is excluded. Comparisons are exploratory.
