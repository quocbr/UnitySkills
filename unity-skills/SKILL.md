---
name: unity-skills
description: Build, review, diagnose, and automate Unity projects with Unity guidance, Nice Wolf Studio's Unity 6.3 patterns, and Besty's live Editor operations. Use for Unity C# and gameplay architecture, Input System, ECS/DOTS, scenes and assets, UI, rendering, physics, packages, tests, builds, or game services.
---

# Unity Skills

1. Identify the project, Unity version, installed packages, and whether the request needs advice, source changes, live Editor work, or a headless command.
2. Open [the unified workflow catalog](references/workflows.md) and use the matching workflow. Its linked guides are part of this skill and can be read directly. The catalog controls routing when a source guide assumes its upstream skill is installed separately or recommends a different execution path.
3. For a live Editor, read [the Editor protocol](EDITOR.md). Confirm the target with `GET /health` and pass `expectInstance` or `expectProject` for writes. Discover exact signatures via `GET /skills/schema?names=...` or scoped `GET /skills/recommend`. Follow the returned mode, surface profile and dry-run policy. Use read-back to verify the result and await compile or reload jobs when returned.
4. When choosing CLI, Pipeline, or REST for the same operation, use one backend and verify its result before any retry. Keep REST and Pipeline permissions separate. If a live operation is blocked by the Editor's policy, follow the stated approval or recovery flow.

For Editor modules outside the combined workflows, use [the module catalog](skills/GUIDE.md). The module references use `skills/<module>/GUIDE.md`; the server or original upstream docs may refer to these as `SKILL.md`. The Besty Python client is at [scripts/unity_skills.py](scripts/unity_skills.py).

The user controls individual REST skills and categories in **UnitySkills → Skills**. When the server reports a disabled skill or group, stop that operation and identify the toggle for the user.
