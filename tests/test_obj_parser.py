from pathlib import Path

from rvatlas.parsers import OBJParser


def test_parse_main_obj():

    obj = Path("examples/input/main.obj")

    mesh, material_library = OBJParser(obj).parse()

    assert mesh.vertex_count == 16356
    assert mesh.uv_count == 4894
    assert mesh.normal_count == 7315
    assert mesh.face_count == 12253

    assert material_library == "main.mtl"