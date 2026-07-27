from rvatlas.atlas.atlas import Atlas
from rvatlas.atlas.uv_mapper import UVMapper
from rvatlas.models.mesh import Mesh


class UVRemapper:
    """
    Remap all mesh UV coordinates into atlas space.
    """

    def __init__(self, mesh: Mesh, atlas: Atlas):
        self.mesh = mesh
        self.atlas = atlas

    def remap(self) -> None:
        """
        Remap every face UV into atlas coordinates.

        A new UV entry is created for every face vertex.
        This avoids problems when the same original UV index
        is shared across multiple materials.
        """

        for face in self.mesh.faces:

            if face.material_name is None:
                continue

            material = self.mesh.materials.get(face.material_name)

            if material is None or material.texture is None:
                continue

            placement = None

            for candidate in self.atlas.placements:

                if candidate.texture == material.texture:
                    placement = candidate
                    break

            if placement is None:
                continue

            for face_vertex in face.vertices:

                if face_vertex.uv_index is None:
                    continue

                original_uv = self.mesh.uvs[face_vertex.uv_index]

                remapped_uv = UVMapper.map_uv(
                    original_uv,
                    self.atlas,
                    placement,
                )

                #
                # Append the remapped UV
                #

                self.mesh.uvs.append(remapped_uv)

                #
                # Point this face to the new UV
                #

                face_vertex.uv_index = len(self.mesh.uvs) - 1