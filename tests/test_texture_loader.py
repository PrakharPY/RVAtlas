from pathlib import Path

from rvatlas.loaders import TextureLoader
from rvatlas.parsers import OBJParser
from rvatlas.parsers.mtl_parser import MTLParser


def test_texture_loader():

    obj = Path("examples/input/main.obj")

    mesh, material_library = OBJParser(obj).parse()

    mtl = obj.parent / material_library

    MTLParser(mesh, mtl).parse()

    TextureLoader(mesh).load()

    assert len(mesh.materials) == 51

    for material in mesh.materials.values():

        if material.texture is None:
            continue

        assert material.texture.width > 0
        assert material.texture.height > 0