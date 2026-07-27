from pathlib import Path

from rvatlas.parsers.obj_parser import OBJParser


def main() -> None:
    obj_path = Path("examples/input/main.obj")

    mesh, material_library = OBJParser(obj_path).parse()

    print("=" * 50)
    print("RVAtlas")
    print("=" * 50)

    print(f"Vertices : {mesh.vertex_count}")
    print(f"UVs      : {mesh.uv_count}")
    print(f"Normals  : {mesh.normal_count}")
    print(f"Faces    : {mesh.face_count}")

    print()
    print(f"Material Library : {material_library}")


if __name__ == "__main__":
    main()