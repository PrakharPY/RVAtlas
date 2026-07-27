from pathlib import Path

from rvatlas.atlas.packers.shelf import ShelfPacker
from rvatlas.loaders.texture_loader import TextureLoader
from rvatlas.parsers.mtl_parser import MTLParser
from rvatlas.parsers.obj_parser import OBJParser


def test_shelf_packer():

    obj_path = Path("examples/input/main.obj")

    mesh, material_library = OBJParser(obj_path).parse()

    mtl_path = obj_path.parent / material_library

    MTLParser(mesh, mtl_path).parse()

    TextureLoader(mesh).load()

    textures = [
        material.texture
        for material in mesh.materials.values()
        if material.texture is not None
    ]

    atlas = ShelfPacker(textures).pack()

    assert len(atlas.placements) == len(textures)

    for placement in atlas.placements:
        assert placement.rectangle.width > 0
        assert placement.rectangle.height > 0