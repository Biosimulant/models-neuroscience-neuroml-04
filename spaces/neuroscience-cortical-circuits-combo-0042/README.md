# COMBO_0042 - Neuroscience Cortical Circuits

## Scientific Question
How do cortical circuit motifs transform and propagate activity?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000929-model`: Neuroscience: Layer6ContinuousNonAccommodatingNestBasketNmlcl000929Model
- `neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000930-model`: Neuroscience: Layer6ContinuousNonAccommodatingNestBasketNmlcl000930Model
- `neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000931-model`: Neuroscience: Layer6ContinuousNonAccommodatingNestBasketNmlcl000931Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000929-model :: neuroml_db:NMLCL000929 :: https://neuroml-db.org/model_info?model_id=NMLCL000929
- neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000930-model :: neuroml_db:NMLCL000930 :: https://neuroml-db.org/model_info?model_id=NMLCL000930
- neuroscience-neuroml-layer-6-continuous-non-accommodating-nest-basket-nmlcl000931-model :: neuroml_db:NMLCL000931 :: https://neuroml-db.org/model_info?model_id=NMLCL000931

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
