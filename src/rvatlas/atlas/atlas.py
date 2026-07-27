"""
Texture atlas model.
"""

from dataclasses import dataclass, field

from .rectangle import Rectangle


@dataclass(slots=True)
class Atlas:
    """
    Represents one texture atlas.
    """

    width: int
    height: int

    rectangles: list[Rectangle] = field(default_factory=list)

    def add(self, rectangle: Rectangle) -> None:
        """
        Add a packed rectangle.
        """

        self.rectangles.append(rectangle)