# Space Plan - neuroscience-cortical-circuits-combo-0042

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000929-model, neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000930-model, neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000931-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
