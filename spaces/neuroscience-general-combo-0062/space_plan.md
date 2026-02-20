# Space Plan - neuroscience-general-combo-0062

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-neuroml-nax-sodium-channel-for-axon-nmlch001610-model, neuroscience-neuroml-nengoneuroml-nengoneuroml-model, neuroscience-neuroml-netpyneshowcase-netpyneshowcase-model, neuroscience-neuroml-neuromlsbmlshowcase-neuromlsbmlshowcase-model

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
