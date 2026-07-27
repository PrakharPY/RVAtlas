from pathlib import Path

from rvatlas.atlas.atlas import Atlas
from rvatlas.atlas.image_generator import AtlasImageGenerator
from rvatlas.atlas.packers.shelf import ShelfPacker
from rvatlas.loaders.texture_loader import TextureLoader
from rvatlas.models.mesh import Mesh
from rvatlas.parsers.mtl_parser import MTLParser
from rvatlas.parsers.obj_parser import OBJParser


def load_mesh(obj_path: Path) -> tuple[Mesh, str | None]:
    """
    Load a Wavefront OBJ together with its material library.
    """

    mesh, material_library = OBJParser(obj_path).parse()

    if material_library is not None:
        mtl_path = obj_path.parent / material_library
        MTLParser(mesh, mtl_path).parse()

    TextureLoader(mesh).load()

    return mesh, material_library


def build_atlas(mesh: Mesh) -> Atlas:
    """
    Pack all textures into an atlas.
    """

    textures = [
        material.texture
        for material in mesh.materials.values()
        if material.texture is not None
    ]

    return ShelfPacker(textures).pack()


def generate_atlas(
    atlas: Atlas,
    output_path: Path,
) -> None:
    """
    Generate atlas image.
    """

    AtlasImageGenerator(atlas).generate(output_path)