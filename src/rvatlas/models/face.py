from dataclasses import dataclass, field


@dataclass(slots=True)
class FaceVertex:
    vertex_index: int
    uv_index: int | None = None
    normal_index: int | None = None


@dataclass(slots=True)
class Face:
    """
    Represents one polygon face.
    """

    vertices: list[FaceVertex] = field(default_factory=list)

    # Name of the material active when this face was parsed.
    material_name: str | None = None