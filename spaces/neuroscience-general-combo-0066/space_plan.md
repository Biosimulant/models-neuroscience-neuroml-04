# Space Plan - neuroscience-general-combo-0066

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-neuroml-nmda-l6nt-l4ss-nmlsy000202-model, neuroscience-neuroml-nmda-l6nt-nrt-nmlsy000203-model, neuroscience-neuroml-nmda-l6nt-supfs-nmlsy000204-model, neuroscience-neuroml-nmda-l6nt-suplts-nmlsy000205-model

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
