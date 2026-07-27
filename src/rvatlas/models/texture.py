"""
Texture model.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Texture:
    """Represents a texture image."""

    path: Path
    width: int = 0
    height: int = 0

    @property
    def name(self) -> str:
        """Return the filename."""

        return self.path.name