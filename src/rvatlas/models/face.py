"""
Face models.

These classes represent polygon faces from a Wavefront OBJ file.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class FaceVertex:
    """
    Represents one vertex reference inside a face.

    OBJ format:

        v
        v/vt
        v//vn
        v/vt/vn
    """

    vertex: int
    uv: int | None = None
    normal: int | None = None


@dataclass(slots=True)
class Face:
    """
    Represents one polygon face.

    Usually a triangle, but quads and n-gons are also supported.
    """

    vertices: list[FaceVertex]
    material: str | None = None

    @property
    def vertex_count(self) -> int:
        """Return the number of vertices in the face."""

        return len(self.vertices)