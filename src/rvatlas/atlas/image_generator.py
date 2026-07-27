"""
Generates a texture atlas image from packed placements.
"""

from pathlib import Path

from PIL import Image

from rvatlas.atlas.atlas import Atlas


class AtlasImageGenerator:
    """
    Creates an atlas image from packed textures.
    """

    def __init__(self, atlas: Atlas):
        self.atlas = atlas

    def generate(self, output_path: Path) -> None:
        """
        Generate and save the atlas image.
        """

        atlas_image = Image.new(
            "RGBA",
            (self.atlas.width, self.atlas.height),
            (0, 0, 0, 0),
        )

        for placement in self.atlas.placements:

            texture = placement.texture
            rect = placement.rectangle

            with Image.open(texture.path) as image:

                atlas_image.paste(
                    image,
                    (rect.x, rect.y),
                )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        atlas_image.save(output_path)