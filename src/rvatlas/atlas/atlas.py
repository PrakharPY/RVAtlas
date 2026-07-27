"""
Texture atlas model.
"""

from dataclasses import dataclass, field

from .placement import Placement


@dataclass(slots=True)
class Atlas:
    """
    Represents one texture atlas.
    """

    width: int
    height: int

    placements: list[Placement] = field(default_factory=list)

    def add(self, placement: Placement) -> None:
        self.placements.append(placement)