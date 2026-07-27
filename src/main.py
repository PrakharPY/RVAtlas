from pathlib import Path

from rvatlas.atlas.image_generator import AtlasImageGenerator
from rvatlas.atlas.packers.shelf import ShelfPacker
from rvatlas.exporters import MTLExporter, OBJExporter
from rvatlas.loaders.texture_loader import TextureLoader
from rvatlas.parsers.mtl_parser import MTLParser
from rvatlas.parsers.obj_parser import OBJParser
from rvatlas.remappers import UVRemapper


def main() -> None:
    # ------------------------------------------------------------------
    # Input / Output paths
    # ------------------------------------------------------------------

    input_dir = Path("examples/input")
    output_dir = Path("examples/output")

    obj_path = input_dir / "main.obj"

    atlas_path = output_dir / "atlas.png"
    obj_output_path = output_dir / "optimized.obj"
    mtl_output_path = output_dir / "optimized.mtl"

    output_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Parse OBJ
    # ------------------------------------------------------------------

    mesh, material_library = OBJParser(obj_path).parse()

    # ------------------------------------------------------------------
    # Parse MTL
    # ------------------------------------------------------------------

    if material_library is not None:
        mtl_path = input_dir / material_library
        MTLParser(mesh, mtl_path).parse()

    # ------------------------------------------------------------------
    # Load textures
    # ------------------------------------------------------------------

    TextureLoader(mesh).load()

    textures = [
        material.texture
        for material in mesh.materials.values()
        if material.texture is not None
    ]

    # ------------------------------------------------------------------
    # Build atlas
    # ------------------------------------------------------------------

    atlas = ShelfPacker(textures).pack()

    # ------------------------------------------------------------------
    # Generate atlas image
    # ------------------------------------------------------------------

    AtlasImageGenerator(atlas).generate(atlas_path)

    # ------------------------------------------------------------------
    # Remap UV coordinates
    # ------------------------------------------------------------------

    UVRemapper(mesh, atlas).remap()

    # ------------------------------------------------------------------
    # Export OBJ + MTL
    # ------------------------------------------------------------------

    OBJExporter(
        mesh,
        obj_output_path,
    ).export()

    MTLExporter(
        mtl_output_path,
        texture_name="atlas.png",
    ).export()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    print("=" * 60)
    print("RVAtlas")
    print("=" * 60)
    print()

    print("Geometry")
    print("-" * 60)
    print(f"Vertices   : {mesh.vertex_count}")
    print(f"UVs        : {mesh.uv_count}")
    print(f"Normals    : {mesh.normal_count}")
    print(f"Faces      : {mesh.face_count}")
    print()

    print("Assets")
    print("-" * 60)
    print(f"Materials  : {len(mesh.materials)}")
    print(f"Textures   : {len(textures)}")
    print()

    print("Atlas")
    print("-" * 60)
    print(f"Width      : {atlas.width}")
    print(f"Height     : {atlas.height}")
    print(f"Placements : {len(atlas.placements)}")
    print()

    print("Generated Files")
    print("-" * 60)
    print(atlas_path)
    print(obj_output_path)
    print(mtl_output_path)

    print()
    print("Done! 🎉")


if __name__ == "__main__":
    main()