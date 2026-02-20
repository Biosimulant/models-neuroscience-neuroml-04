# Space Plan - neuroscience-general-combo-0059

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-neuroml-nap-persistent-sodium-nmlch001401-model, neuroscience-neuroml-nap-persistent-sodium-nmlch001480-model, neuroscience-neuroml-nar-resurgent-sodium-nmlch000097-model, neuroscience-neuroml-nat-transient-sodium-nmlch000098-model

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
