---
name: unity-skills
description: Use for Unity-specific coding and code review, including writing, reading, debugging, refactoring, or testing C# scripts that involve Unity APIs, gameplay behavior, or Editor tools. Applies when the Unity project provides context even if the request only says "sửa logic", "review script này", or names a .cs file. Also use for Unity scenes, assets, UI, Input System, ECS/DOTS, rendering, physics, packages, builds, or game services.
---

# Unity Skills

1. Identify the project, Unity version, installed packages, and whether the request needs advice, source changes, live Editor work, or a headless command.
2. For Unity C# tasks, start with [C# implementation and code review](references/workflows.md#c-implementation-and-code-review) and read the affected source and callers. Keep analysis and read-only reviews in source unless they need live Editor data. For other tasks, open the matching section in [the unified workflow catalog](references/workflows.md). Its linked guides are part of this skill. Follow the catalog when a guide assumes a separate skill or recommends a different execution path. If no guidance fits the task, use a more suitable skill or proceed with the usual coding or code review workflow.
3. For a live Editor, read [the Editor protocol](EDITOR.md). Confirm the target with `GET /health` and pass `expectInstance` or `expectProject` for writes. Discover exact signatures via `GET /skills/schema?names=...` or scoped `GET /skills/recommend`. Follow the returned mode, surface profile and dry-run policy. Use read-back to verify the result and await compile or reload jobs when returned.
4. When choosing CLI, Pipeline, or REST for the same operation, use one backend and verify its result before any retry. Keep REST and Pipeline permissions separate. If a live operation is blocked by the Editor's policy, follow the stated approval or recovery flow.

For Editor modules outside the combined workflows, use [the module catalog](skills/GUIDE.md). The module references use `skills/<module>/GUIDE.md`; the server or original upstream docs may refer to these as `SKILL.md`. The Besty Python client is at [scripts/unity_skills.py](scripts/unity_skills.py).

The user controls individual REST skills and categories in **UnitySkills → Skills**. When the server reports a disabled skill or group, stop that operation and identify the toggle for the user.
