"""
Geometry primitives used throughout RVAtlas.

These classes represent the basic geometric data found in
Wavefront OBJ files.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Vertex:
    """Represents a 3D vertex."""

    x: float
    y: float
    z: float


@dataclass(slots=True)
class UV:
    """Represents a 2D texture coordinate."""

    u: float
    v: float


@dataclass(slots=True)
class Normal:
    """Represents a vertex normal."""

    x: float
    y: float
    z: float