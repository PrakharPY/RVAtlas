"""
Rectangle model used by atlas packing algorithms.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Rectangle:
    """
    Represents a rectangle inside an atlas.
    """

    x: int
    y: int
    width: int
    height: int

    @property
    def right(self) -> int:
        return self.x + self.width

    @property
    def bottom(self) -> int:
        return self.y + self.height

    def intersects(self, other: "Rectangle") -> bool:
        """
        Return True if two rectangles overlap.
        """

        return not (
            self.right <= other.x
            or other.right <= self.x
            or self.bottom <= other.y
            or other.bottom <= self.y
        )