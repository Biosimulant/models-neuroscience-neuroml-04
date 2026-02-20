# Space Prompt - neuroscience-general-combo-0048

Create a scientifically coherent **neuroscience / general** comparative space using:
- Base models: neuroscience-neuroml-na-slowly-inactivating-sodium-nmlch000125-model, neuroscience-neuroml-na-sodium-channel-component-nmlcp001647-model, neuroscience-neuroml-na-sodium-nmlch000005-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
