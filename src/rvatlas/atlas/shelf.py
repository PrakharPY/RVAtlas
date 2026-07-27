"""
Simple Shelf atlas packing algorithm.
"""

from rvatlas.atlas.atlas import Atlas
from rvatlas.atlas.packers.base import BasePacker
from rvatlas.atlas.rectangle import Rectangle
from rvatlas.models.texture import Texture


class ShelfPacker(BasePacker):
    """
    Packs textures row by row into an atlas.
    """

    def __init__(
        self,
        textures: list[Texture],
        atlas_width: int = 4096,
    ) -> None:

        self.textures = textures

        self.atlas_width = atlas_width

    def pack(self) -> Atlas:

        atlas = Atlas(
            width=self.atlas_width,
            height=0,
        )

        x = 0
        y = 0

        shelf_height = 0

        for texture in self.textures:

            if texture.width == 0 or texture.height == 0:
                raise ValueError(
                    f"Texture not loaded: {texture.path}"
                )

            #
            # Doesn't fit on this shelf?
            #
            if x + texture.width > self.atlas_width:

                x = 0

                y += shelf_height

                shelf_height = 0

            rect = Rectangle(
                x=x,
                y=y,
                width=texture.width,
                height=texture.height,
            )

            atlas.add(rect)

            x += texture.width

            shelf_height = max(
                shelf_height,
                texture.height,
            )

        atlas.height = y + shelf_height

        return atlas