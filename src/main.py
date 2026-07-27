from pathlib import Path

from rvatlas.loaders.texture_loader import TextureLoader
from rvatlas.parsers.mtl_parser import MTLParser
from rvatlas.parsers.obj_parser import OBJParser


def main() -> None:
    # Path to the OBJ model
    obj_path = Path("examples/input/main.obj")

    # Parse OBJ
    mesh, material_library = OBJParser(obj_path).parse()

    # Parse MTL
    if material_library is not None:
        mtl_path = obj_path.parent / material_library
        MTLParser(mesh, mtl_path).parse()

    # Load texture information
    TextureLoader(mesh).load()

    print("=" * 60)
    print("RVAtlas")
    print("=" * 60)

    print("Geometry")
    print("-" * 60)
    print(f"Vertices : {mesh.vertex_count}")
    print(f"UVs      : {mesh.uv_count}")
    print(f"Normals  : {mesh.normal_count}")
    print(f"Faces    : {mesh.face_count}")

    print()

    print("Assets")
    print("-" * 60)
    print(f"Material Library : {material_library}")
    print(f"Materials        : {len(mesh.materials)}")

    print()

    print("Sample Materials")
    print("-" * 60)

    # Show only the first five materials
    for material in list(mesh.materials.values())[:5]:

        if material.texture is None:
            print(f"{material.name:<25} -> No Texture")
            continue

        texture = material.texture

        print(
            f"{material.name:<25}"
            f" -> {texture.path.name}"
            f" ({texture.width} x {texture.height})"
        )


if __name__ == "__main__":
    main()