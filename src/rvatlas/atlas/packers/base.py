"""
Base class for atlas packing algorithms.
"""

from abc import ABC, abstractmethod

from rvatlas.atlas.atlas import Atlas


class BasePacker(ABC):
    """
    Base interface for atlas packers.
    """

    @abstractmethod
    def pack(self) -> Atlas:
        """
        Pack textures into an atlas.
        """
        raise NotImplementedError