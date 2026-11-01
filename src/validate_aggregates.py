"""Inspect saved aggregates. No raw-data analysis, model calls, fits or bootstrap."""
from pathlib import Path
import json, math, csv
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'public_data/aggregate_results.json').read_text(encoding='utf8'))
views=json.loads((ROOT/'public_data/feature_views.json').read_text(encoding='utf8'))['views']
assert [v['columns'] for v in views]==[0,11,12,9,18,23,25,34,34]
assert all(len(v['features'])==v['columns'] for v in views)
assert sum(d['counts']['split_counts'].values())==224
assert d['counts']['final_at_risk_successes']+d['counts']['final_at_risk_failures']==124
assert d['counts']['primary_calibration_n']==d['counts']['primary_calibration_failures']==30
assert len(d['metrics'])==18
for m in d['metrics']:
    assert m['n']==m['successes']+m['failures']==124
    assert m['successes']==4 and m['failures']==120
    assert math.isfinite(m['log_loss']) and 0<=m['Brier']<=1
for p in d['gain_points']:
    get=lambda v: next(m['log_loss'] for m in d['metrics'] if m['scope']==p['scope'] and m['view']==v)
    assert math.isclose(get(p['baseline'])-get('task_relevance_augmented'),p['mean'],abs_tol=1e-12)
    assert p['lo']<0<p['hi']
with (ROOT/'public_data/view_metrics.csv').open(encoding='utf8',newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==18
for row,m in zip(rows,d['metrics']):
    assert row['view']==m['view'] and row['scope']==m['scope']
    assert float(row['log_loss'])==m['log_loss'] and float(row['Brier'])==m['Brier']
print('PASS: 18 saved metric rows, nine views, split/count identities, four paired differences, and CSV/JSON agreement. This does not rederive private experimental results.')
