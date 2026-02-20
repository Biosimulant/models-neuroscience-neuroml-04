# Space Prompt - neuroscience-general-combo-0060

Create a scientifically coherent **neuroscience / general** comparative space using:
- Base models: neuroscience-neuroml-nata-fast-inactivating-sodium-nmlch000110-model, neuroscience-neuroml-nata-fast-inactivating-sodium-nmlch001398-model, neuroscience-neuroml-nats-fast-inactivating-sodium-nmlch000111-model, neuroscience-neuroml-nats-fast-inactivating-sodium-nmlch001490-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
