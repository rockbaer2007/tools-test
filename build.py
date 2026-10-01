"""Build the reference tool package as a regular ZIP archive."""

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "package"
manifest = json.loads((SOURCE / "manifest.json").read_text(encoding="utf-8"))
assert manifest["format"] == "ha-grafik-tool-package"
assert manifest["apiVersion"] == "0.1"
assets = {manifest["icon"], *(item["icon"] for item in manifest["tools"] if "icon" in item)}
for asset in assets:
    if not asset.startswith("icons/") or not (SOURCE / asset).is_file():
        raise ValueError(f"Referenced icon is missing: {asset}")
OUTPUT = ROOT / "dist" / f"tools-test-{manifest['version']}.tp.zip"
OUTPUT.parent.mkdir(exist_ok=True)
with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as archive:
    archive.write(SOURCE / "manifest.json", "manifest.json")
    for asset in sorted(assets):
        archive.write(SOURCE / asset, asset)
print(OUTPUT)
