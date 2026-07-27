"""
rvatlas.parsers.obj_parser

Wavefront OBJ parser used by RVAtlas.

Supported features:
- Vertices
- Texture coordinates
- Normals
- Faces
- Material library
- Material assignments

Unsupported (for now):
- Groups (g)
- Objects (o)
- Smoothing groups (s)
- Parameter-space vertices (vp)
"""

from pathlib import Path

from rvatlas.models.face import Face, FaceVertex
from rvatlas.models.geometry import Vertex, UV, Normal
from rvatlas.models.mesh import Mesh


class OBJParser:
    """
    Parses a Wavefront OBJ file into a Mesh object.
    """

    def __init__(self, path: str | Path):

        self.path = Path(path)

        self.mesh = Mesh()

        self.material_library: str | None = None

        self.current_material: str | None = None

    def parse(self) -> tuple[Mesh, str | None]:
        """
        Parse the OBJ file.

        Returns
        -------
        tuple
            (Mesh, material library filename)
        """

        with self.path.open(
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            for line in file:

                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if line.startswith("v "):
                    self._parse_vertex(line)

                elif line.startswith("vt "):
                    self._parse_uv(line)

                elif line.startswith("vn "):
                    self._parse_normal(line)

                elif line.startswith("mtllib "):
                    self.material_library = line.split(
                        maxsplit=1
                    )[1]

                elif line.startswith("usemtl "):
                    self.current_material = line.split(
                        maxsplit=1
                    )[1]

                elif line.startswith("f "):
                    self._parse_face(line)

        return self.mesh, self.material_library

    def _parse_vertex(self, line: str) -> None:
        """Parse a vertex."""

        _, x, y, z = line.split()

        self.mesh.vertices.append(
            Vertex(
                float(x),
                float(y),
                float(z),
            )
        )

    def _parse_uv(self, line: str) -> None:
        """Parse a texture coordinate."""

        parts = line.split()

        self.mesh.uvs.append(
            UV(
                float(parts[1]),
                float(parts[2]),
            )
        )

    def _parse_normal(self, line: str) -> None:
        """Parse a normal."""

        _, x, y, z = line.split()

        self.mesh.normals.append(
            Normal(
                float(x),
                float(y),
                float(z),
            )
        )

    def _parse_face(self, line: str) -> None:
        """Parse one face."""

        face_vertices: list[FaceVertex] = []

        for token in line.split()[1:]:

            parts = token.split("/")

            vertex = int(parts[0])

            uv = None
            normal = None

            if len(parts) > 1 and parts[1]:
                uv = int(parts[1])

            if len(parts) > 2 and parts[2]:
                normal = int(parts[2])

            face_vertices.append(
                FaceVertex(
                    vertex=vertex,
                    uv=uv,
                    normal=normal,
                )
            )

        self.mesh.faces.append(
            Face(
                vertices=face_vertices,
                material=self.current_material,
            )
        )