# Space Prompt - neuroscience-general-combo-0045

Create a scientifically coherent **neuroscience / general** comparative space using:
- Base models: neuroscience-neuroml-low-threshold-spiking-lts-nmlcl001126-model, neuroscience-neuroml-main-olfactory-bulb-granule-cell-nmlcl001128-model, neuroscience-neuroml-main-olfactory-bulb-mitral-cell-1-nmlcl001129-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
