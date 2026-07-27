"""
rvatlas.parsers.mtl_parser

Wavefront MTL parser used by RVAtlas.

Supported features:
- newmtl
- map_Kd

Unsupported (for now):
- Ka
- Kd
- Ks
- Ns
- Ni
- illum
- d
- Tr
- map_Bump
- map_Ks
"""

from pathlib import Path

from rvatlas.models.material import Material
from rvatlas.models.mesh import Mesh
from rvatlas.models.texture import Texture


class MTLParser:
    """
    Parses a Wavefront MTL file and populates Mesh.materials.
    """

    def __init__(
        self,
        mesh: Mesh,
        material_library: str | Path,
    ) -> None:
        self.mesh = mesh

        self.path = Path(material_library)

        self.current_material: Material | None = None

    def parse(self) -> None:
        """
        Parse the MTL file.
        """

        with self.path.open(
            "r",
            encoding="utf-8",
            errors="ignore",
        ) as file:

            for line in file:

                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if line.startswith("newmtl "):
                    self._parse_material(line)

                elif line.startswith("map_Kd "):
                    self._parse_diffuse_texture(line)

    def _parse_material(self, line: str) -> None:
        """
        Parse a material declaration.
        """

        name = line.split(maxsplit=1)[1]

        material = Material(name=name)

        self.mesh.materials[name] = material

        self.current_material = material

    def _parse_diffuse_texture(self, line: str) -> None:
        """
        Parse the diffuse texture (map_Kd).
        """

        if self.current_material is None:
            return

        texture_name = line.split(maxsplit=1)[1]

        texture_path = self.path.parent / texture_name

        self.current_material.texture = Texture(
            path=texture_path
        )