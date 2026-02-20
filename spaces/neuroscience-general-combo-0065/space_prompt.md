# Space Prompt - neuroscience-general-combo-0065

Create a scientifically coherent **neuroscience / general** comparative space using:
- Base models: neuroscience-neuroml-nmda-l4ss-pyr-nmlsy000189-model, neuroscience-neuroml-nmda-l6nt-deepfs-nmlsy000199-model, neuroscience-neuroml-nmda-l6nt-deeplts-nmlsy000200-model, neuroscience-neuroml-nmda-l6nt-deeppyr-nmlsy000201-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
