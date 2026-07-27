"""
Represents the placement of a texture inside an atlas.
"""

from dataclasses import dataclass

from rvatlas.atlas.rectangle import Rectangle
from rvatlas.models.texture import Texture


@dataclass(slots=True)
class Placement:
    texture: Texture
    rectangle: Rectangle