"""
Material model.
"""

from dataclasses import dataclass

from .texture import Texture


@dataclass(slots=True)
class Material:
    """Represents a material from an MTL file."""

    name: str
    texture: Texture | None = None