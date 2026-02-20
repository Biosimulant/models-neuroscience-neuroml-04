# COMBO_0069 - Neuroscience Cortical Circuits

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
- `neuroscience-neuroml-layer-6-continuous-accommodating-double-bouquet-nmlcl000616-model`: Neuroscience: Layer6ContinuousAccommodatingDoubleBouquetNmlcl000616Model
- `neuroscience-neuroml-layer-6-continuous-accommodating-martinotti-cell-nmlcl000617-model`: Neuroscience: Layer6ContinuousAccommodatingMartinottiCellNmlcl000617Model
- `neuroscience-neuroml-layer-6-continuous-accommodating-martinotti-cell-nmlcl000618-model`: Neuroscience: Layer6ContinuousAccommodatingMartinottiCellNmlcl000618Model
- `neuroscience-neuroml-layer-6-continuous-accommodating-martinotti-cell-nmlcl000619-model`: Neuroscience: Layer6ContinuousAccommodatingMartinottiCellNmlcl000619Model

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
- neuroscience-neuroml-layer-6-continuous-accommodating-double-bouquet-nmlcl000616-model :: neuroml_db:NMLCL000616 :: https://neuroml-db.org/model_info?model_id=NMLCL000616
- neuroscience-neuroml-layer-6-continuous-accommodating-martinotti-cell-nmlcl000617-model :: neuroml_db:NMLCL000617 :: https://neuroml-db.org/model_info?model_id=NMLCL000617
- neuroscience-neuroml-layer-6-continuous-accommodating-martinotti-cell-nmlcl000618-model :: neuroml_db:NMLCL000618 :: https://neuroml-db.org/model_info?model_id=NMLCL000618
- neuroscience-neuroml-layer-6-continuous-accommodating-martinotti-cell-nmlcl000619-model :: neuroml_db:NMLCL000619 :: https://neuroml-db.org/model_info?model_id=NMLCL000619

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
