#!/usr/bin/env python3
"""Refresh the unified template's supporting files from the pinned source trees."""

import os
import re
from hashlib import sha256
from pathlib import Path
from shutil import copyfile
from urllib.parse import unquote
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "unity-skills"
OFFICIAL = ROOT / "upstream" / "unity-technologies-skills"
BESTY = ROOT / "upstream" / "besty-unity-skills"
NICE_WOLF = ROOT / "upstream" / "nice-wolf-studio-unity-claude-skills"
BESTY_TEMPLATE = BESTY / "SkillsForUnity" / "unity-skills~"
PACKAGE_ARCHIVE = BESTY_TEMPLATE.with_name("workbench-skill~") / "template.zip"
REVISION = "workbench-revision.txt"
LINK = re.compile(r"(\]\()([^\s)#]+)(?=[)#\s])")


def refresh():
    copies = {}
    nice_wolf_reference = TEMPLATE / "references" / "nice-wolf-studio"
    for source_root, destination_root in (
        (BESTY_TEMPLATE, TEMPLATE),
        (OFFICIAL / "skills", TEMPLATE / "references" / "unity-technologies"),
        (NICE_WOLF / "skills", nice_wolf_reference),
        (NICE_WOLF / "unity-ops" / "skills", nice_wolf_reference),
    ):
        for source in source_root.rglob("*"):
            if not source.is_file() or "__pycache__" in source.parts or source.name == "agent_config.json":
                continue
            destination = destination_root / source.relative_to(source_root)
            if source == BESTY_TEMPLATE / "SKILL.md":
                destination = TEMPLATE / "EDITOR.md"
            elif source.name == "SKILL.md":
                destination = destination.with_name("GUIDE.md")
            copies[source] = destination

    copies[BESTY / "LICENSE"] = TEMPLATE / "LICENSE"
    copies[OFFICIAL / "LICENSE.md"] = TEMPLATE / "references" / "unity-technologies" / "LICENSE.md"
    copies[NICE_WOLF / "LICENSE"] = nice_wolf_reference / "LICENSE"

    for source, destination in copies.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix != ".md":
            copyfile(source, destination)
            continue

        def link_to_reference(match):
            url = match[2]
            if ":" in url or url.startswith("/"):
                return match[0]
            target = copies.get((source.parent / unquote(url)).resolve())
            if target is None:
                return match[0]
            relative = Path(os.path.relpath(target, destination.parent)).as_posix()
            return match[1] + relative.replace(" ", "%20")

        text = source.read_text(encoding="utf-8")
        destination.write_bytes(LINK.sub(link_to_reference, text).encode("utf-8"))

    PACKAGE_ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    revision = sha256()
    with ZipFile(PACKAGE_ARCHIVE, "w") as archive:
        for source in sorted(TEMPLATE.rglob("*"), key=lambda path: path.relative_to(TEMPLATE).as_posix()):
            if not source.is_file() or "__pycache__" in source.parts or source.name in ("agent_config.json", REVISION):
                continue
            name = source.relative_to(TEMPLATE).as_posix()
            content = source.read_bytes()
            revision.update(name.encode("utf-8") + b"\0" + sha256(content).digest())
            archive.writestr(ZipInfo(name), content, compress_type=ZIP_DEFLATED)

        revision_text = revision.hexdigest() + "\n"
        archive.writestr(ZipInfo(REVISION), revision_text, compress_type=ZIP_DEFLATED)
    (TEMPLATE / REVISION).write_bytes(revision_text.encode("ascii"))


if __name__ == "__main__":
    refresh()
