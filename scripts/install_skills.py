#!/usr/bin/env python3
"""Install the unified unity-skills skill into a Unity project."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from shutil import copytree, ignore_patterns
from tempfile import TemporaryDirectory, mkdtemp

from refresh_skill_references import BESTY, BESTY_TEMPLATE, OFFICIAL, ROOT, TEMPLATE
AGENT_DIRECTORIES = {"codex": ".agents", "claude-code": ".claude"}
IGNORED = ignore_patterns("__pycache__", "*.pyc", "agent_config.json")


def same_file(left, right):
    return left.is_file() and left.read_bytes() == right.read_bytes()


def matches(template, installed):
    return installed.is_dir() and all(
        same_file(installed / path.relative_to(template), path)
        for path in template.rglob("*")
        if path.is_file() and not IGNORED(path.parent, [path.name]) and "__pycache__" not in path.parts
    )


def legacy_skills(destination):
    legacy = []
    for source in sorted((OFFICIAL / "skills").iterdir()):
        installed = destination / source.name
        entry = source / "SKILL.md"
        installed_entry = installed / entry.name
        if not entry.is_file() or not installed_entry.is_file():
            continue
        if same_file(installed_entry, entry) or same_file(installed / "LICENSE.md", OFFICIAL / "LICENSE.md"):
            legacy.append(installed)

    old_besty = destination / TEMPLATE.name
    old_entry = same_file(old_besty / "SKILL.md", BESTY_TEMPLATE / "SKILL.md")
    overlaid = same_file(old_besty / "SKILL.md", TEMPLATE / "SKILL.md") and same_file(
        old_besty / "skills" / "SKILL.md", BESTY_TEMPLATE / "skills" / "SKILL.md"
    )
    if old_entry or overlaid:
        legacy.append(old_besty)
    return legacy


def install(project, agent, migrate=False):
    if not (project / "Assets").is_dir() or not (project / "Packages" / "manifest.json").is_file():
        raise ValueError(f"Not a Unity project: {project}")

    destination = project / AGENT_DIRECTORIES[agent] / "skills"
    if project not in destination.resolve().parents:
        raise ValueError(f"Skill directory must be inside the project: {destination}")
    if set(TEMPLATE.rglob("SKILL.md")) != {TEMPLATE / "SKILL.md"} or not (TEMPLATE / "EDITOR.md").is_file():
        raise ValueError("The unified template must contain one skill entry point and the Editor protocol")

    legacy = legacy_skills(destination)
    installed = destination / TEMPLATE.name
    already_present = installed not in legacy and matches(TEMPLATE, installed)
    if not already_present and installed not in legacy and same_file(installed / "EDITOR.md", TEMPLATE / "EDITOR.md"):
        if (installed / "references" / "workflows.md").is_file():
            legacy.append(installed)
    if (installed.exists() or installed.is_symlink()) and not already_present and installed not in legacy:
        raise FileExistsError(f"Existing skill differs. Move it before retrying: {installed}")
    if legacy and not migrate:
        raise FileExistsError(f"Found {len(legacy)} previous Unity skill installs. Rerun with --migrate to back them up and update.")

    destination.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".unity-skills-", dir=destination) as temporary:
        staged = Path(temporary) / TEMPLATE.name
        if not already_present:
            copytree(TEMPLATE, staged, ignore=IGNORED)
            version = json.loads((BESTY / "SkillsForUnity" / "package.json").read_text(encoding="utf-8"))["version"]
            config = {"agentId": agent, "version": version, "installedAt": datetime.now(timezone.utc).isoformat()}
            (staged / "scripts" / "agent_config.json").write_text(
                json.dumps(config, indent=2) + "\n", encoding="utf-8"
            )

        if legacy:
            backup = Path(mkdtemp(prefix=".unity-skills-backup-", dir=destination.parent))
            moved = []
            try:
                for path in legacy:
                    path.rename(backup / path.name)
                    moved.append(path)
                if not already_present:
                    staged.rename(installed)
            except OSError:
                for path in reversed(moved):
                    if not path.exists() and not path.is_symlink():
                        (backup / path.name).rename(path)
                raise
            print(f"Backed up {len(legacy)} previous skill installs to {backup}")
        elif not already_present:
            staged.rename(installed)

    print(f"{installed}: {'already present' if already_present else 'installed'}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=ROOT, help="Unity project (default: this repository)")
    parser.add_argument("--agent", choices=AGENT_DIRECTORIES, default="codex")
    parser.add_argument("--migrate", action="store_true", help="Back up recognized previous Unity skills before installing")
    args = parser.parse_args()
    try:
        install(args.project.resolve(), args.agent, args.migrate)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
