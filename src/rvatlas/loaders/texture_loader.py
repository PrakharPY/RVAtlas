"""
Texture loader.

Loads texture metadata from image files.
"""

from PIL import Image

from rvatlas.models.mesh import Mesh


class TextureLoader:
    """
    Loads texture information for every material in a mesh.
    """

    def __init__(self, mesh: Mesh) -> None:
        self.mesh = mesh

    def load(self) -> None:

        for material in self.mesh.materials.values():

            if material.texture is None:
                continue

            path = material.texture.path

            if not path.exists():
                print(f"[WARNING] Missing texture: {path}")
                continue

            with Image.open(path) as image:

                material.texture.width = image.width
                material.texture.height = image.height