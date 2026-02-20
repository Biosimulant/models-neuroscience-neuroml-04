# Space Plan - neuroscience-general-combo-0064

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-neuroml-nmda-frbpyr-supfs-nmlsy000185-model, neuroscience-neuroml-nmda-frbpyr-suplts-nmlsy000186-model, neuroscience-neuroml-nmda-l4ss-in-nmlsy000187-model, neuroscience-neuroml-nmda-l4ss-l4ss-nmlsy000188-model

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
