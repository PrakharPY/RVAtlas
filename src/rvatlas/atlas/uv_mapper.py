"""
UV remapping utilities.
"""

from rvatlas.atlas.atlas import Atlas
from rvatlas.models.geometry import UV


class UVMapper:
    """
    Maps UV coordinates from individual textures
    into atlas coordinates.
    """

    @staticmethod
    def map_uv(
        uv: UV,
        atlas: Atlas,
        placement,
    ) -> UV:
        """
        Return a new UV mapped into atlas space.
        """

        rect = placement.rectangle

        atlas_u = (
            rect.x + uv.u * rect.width
        ) / atlas.width

        atlas_v = (
            rect.y + uv.v * rect.height
        ) / atlas.height

        return UV(
            u=atlas_u,
            v=atlas_v,
        )