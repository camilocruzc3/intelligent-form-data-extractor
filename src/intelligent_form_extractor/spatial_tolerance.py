"""Generic coordinate-alignment utilities for form field association."""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from statistics import mean
from typing import Iterable


@dataclass(frozen=True)
class CoordinatePair:
    """Observed and reference coordinates for one anchor field."""

    observed_x: float
    observed_y: float
    reference_x: float
    reference_y: float


@dataclass(frozen=True)
class ToleranceResult:
    """Calculated document displacement and final matching tolerance."""

    offset_x: float
    offset_y: float
    tolerance_x: int
    tolerance_y: int
    anchors_used: int


def calculate_dynamic_tolerance(
    anchors: Iterable[CoordinatePair],
    *,
    extra_margin: int = 2,
    default_tolerance: int = 10,
) -> ToleranceResult:
    """Estimate layout displacement and matching tolerance from anchor fields.

    The average difference between observed and reference coordinates estimates
    the page displacement. The largest residual distance after alignment defines
    the required tolerance, with a small configurable safety margin.
    """

    anchor_list = list(anchors)
    if extra_margin < 0:
        raise ValueError("extra_margin must be non-negative")
    if default_tolerance <= 0:
        raise ValueError("default_tolerance must be positive")

    if not anchor_list:
        return ToleranceResult(
            offset_x=0.0,
            offset_y=0.0,
            tolerance_x=default_tolerance,
            tolerance_y=default_tolerance,
            anchors_used=0,
        )

    differences_x = [
        anchor.observed_x - anchor.reference_x for anchor in anchor_list
    ]
    differences_y = [
        anchor.observed_y - anchor.reference_y for anchor in anchor_list
    ]

    offset_x = mean(differences_x)
    offset_y = mean(differences_y)

    residuals_x = [
        abs((anchor.reference_x + offset_x) - anchor.observed_x)
        for anchor in anchor_list
    ]
    residuals_y = [
        abs((anchor.reference_y + offset_y) - anchor.observed_y)
        for anchor in anchor_list
    ]

    return ToleranceResult(
        offset_x=offset_x,
        offset_y=offset_y,
        tolerance_x=max(1, ceil(max(residuals_x)) + extra_margin),
        tolerance_y=max(1, ceil(max(residuals_y)) + extra_margin),
        anchors_used=len(anchor_list),
    )
