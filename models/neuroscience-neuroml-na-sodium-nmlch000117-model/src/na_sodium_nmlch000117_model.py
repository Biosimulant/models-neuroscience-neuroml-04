# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""Auto-generated NeuroML BioModule wrapper for Na Sodium.

Source: neuroml_db:NMLCH000117
Original: https://neuroml-db.org/model_info?model_id=NMLCH000117
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional, Set, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - typing only
    from biosim import BioWorld

import biosim
from biosim.signals import BioSignal, SignalMetadata

class NeuromlNaSodium2(biosim.BioModule):
    """BioModule wrapper for NeuroML model: Na Sodium."""

    def __init__(self, model_path: str = "data/render_xml_file.nml", min_dt: float = 0.001) -> None:
        self.min_dt = min_dt
        self._model_path = Path(__file__).parent.parent / model_path
        self._t = 0.0
        self._nml_doc = None
        self._outputs: Dict[str, BioSignal] = {}

    def setup(self, config: Optional[Dict[str, Any]] = None) -> None:
        from pyneuroml import pynml

        self._nml_doc = pynml.read_neuroml2_file(str(self._model_path))
        self._t = 0.0

    def reset(self) -> None:
        self._t = 0.0
        self._outputs = {}

    def inputs(self) -> Set[str]:
        return set()

    def outputs(self) -> Set[str]:
        return {"state"}

    def advance_to(self, t: float) -> None:
        """Advance simulation to time *t* using pyNeuroML."""
        if self._nml_doc is None:
            self.setup()

        self._t = t

        model_type = self._detect_model_type()
        state_data: Dict[str, Any] = {"t": t, "type": model_type}

        if model_type == "single-cell" and self._nml_doc.cells:
            cell = self._nml_doc.cells[0]
            state_data["cell_id"] = cell.id
            if hasattr(cell, "biophysical_properties") and cell.biophysical_properties:
                bp = cell.biophysical_properties
                mechs = []
                if hasattr(bp, "membrane_properties") and bp.membrane_properties:
                    mp = bp.membrane_properties
                    if hasattr(mp, "channel_densities"):
                        mechs = [cd.id for cd in (mp.channel_densities or [])]
                state_data["mechanisms"] = mechs
            state_data["morphology_segments"] = (
                len(cell.morphology.segments) if cell.morphology and cell.morphology.segments else 0
            )

        elif model_type == "network" and self._nml_doc.networks:
            net = self._nml_doc.networks[0]
            state_data["network_id"] = net.id
            pops = getattr(net, "populations", []) or []
            state_data["populations"] = len(pops)
            state_data["pop_ids"] = [p.id for p in pops]

        elif model_type == "ion-channel":
            channels = list(getattr(self._nml_doc, "ion_channel_hhs", []) or [])
            channels += list(getattr(self._nml_doc, "ion_channel", []) or [])
            state_data["channel_count"] = len(channels)
            state_data["channel_ids"] = [ch.id for ch in channels]

        elif model_type == "morphology" and self._nml_doc.morphology:
            morph = self._nml_doc.morphology[0] if isinstance(self._nml_doc.morphology, list) else self._nml_doc.morphology
            state_data["morphology_id"] = getattr(morph, "id", "unknown")
            state_data["segments"] = len(morph.segments) if hasattr(morph, "segments") and morph.segments else 0

        source_name = getattr(self, "_world_name", self.__class__.__name__)
        self._outputs = {
            "state": BioSignal(
                source=source_name,
                name="state",
                value=state_data,
                time=t,
                metadata=SignalMetadata(
                    description=f"NeuroML {model_type} model state",
                    kind="state",
                ),
            )
        }

    def get_outputs(self) -> Dict[str, BioSignal]:
        return dict(self._outputs)

    def visualize(self) -> Optional[Dict[str, Any]]:
        """Generate visualization from NeuroML model structure."""
        if self._nml_doc is None:
            return None

        model_type = self._detect_model_type()
        state = self._outputs.get("state")
        value = state.value if state and isinstance(getattr(state, "value", None), dict) else {}

        if model_type == "single-cell":
            lines = [
                f"NeuroML Single Cell: {value.get('cell_id', 'unknown')}",
                f"Time: {self._t}s",
                f"Segments: {value.get('morphology_segments', 0)}",
                f"Mechanisms: {len(value.get('mechanisms', []))}",
            ]
        elif model_type == "network":
            lines = [
                f"NeuroML Network: {value.get('network_id', 'unknown')}",
                f"Time: {self._t}s",
                f"Populations: {value.get('populations', 0)}",
            ]
        elif model_type == "ion-channel":
            lines = [
                f"NeuroML Ion Channel",
                f"Time: {self._t}s",
                f"Channels: {value.get('channel_count', 0)}",
            ]
        else:
            lines = [
                f"NeuroML Model ({model_type})",
                f"Time: {self._t}s",
            ]

        return {
            "render": "text",
            "data": {"text": "\n".join(lines)},
            "description": f"NeuroML {model_type} model",
        }

    def _detect_model_type(self) -> str:
        """Detect NeuroML model type from document structure."""
        if self._nml_doc is None:
            return "unknown"
        if hasattr(self._nml_doc, "cells") and self._nml_doc.cells:
            return "single-cell"
        if hasattr(self._nml_doc, "networks") and self._nml_doc.networks:
            return "network"
        if (hasattr(self._nml_doc, "ion_channel_hhs") and self._nml_doc.ion_channel_hhs) or \
                (hasattr(self._nml_doc, "ion_channel") and self._nml_doc.ion_channel):
            return "ion-channel"
        if hasattr(self._nml_doc, "morphology") and self._nml_doc.morphology:
            return "morphology"
        return "other"

# Canonical alias for stable entrypoint naming.
NaSodiumNmlch000117Model = NeuromlNaSodium2
