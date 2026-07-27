"""
Mesh model.
"""

from dataclasses import dataclass, field

from .face import Face
from .geometry import Normal, UV, Vertex
from .material import Material


@dataclass(slots=True)
class Mesh:
    """
    Represents an OBJ mesh.
    """

    vertices: list[Vertex] = field(default_factory=list)

    uvs: list[UV] = field(default_factory=list)

    normals: list[Normal] = field(default_factory=list)

    faces: list[Face] = field(default_factory=list)

    materials: dict[str, Material] = field(default_factory=dict)

    @property
    def triangle_count(self) -> int:
        """
        Return the number of triangular faces.

        Faces with more than three vertices are not triangulated yet.
        """

        return sum(1 for face in self.faces if face.vertex_count == 3)

    @property
    def vertex_count(self) -> int:
        return len(self.vertices)

    @property
    def uv_count(self) -> int:
        return len(self.uvs)

    @property
    def normal_count(self) -> int:
        return len(self.normals)

    @property
    def face_count(self) -> int:
        return len(self.faces)