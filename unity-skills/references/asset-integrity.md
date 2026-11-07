# Unity asset integrity after source edits

Use this check after creating, moving, renaming, or deleting Unity assets outside the Editor. Keep an existing `.meta` beside the asset it identifies; a newly created file may receive a `.meta` during the next Unity import. The checker is read-only and applies to a project with `Assets/` and `ProjectSettings/`.

```powershell
python unity-skills/scripts/check_unity_project.py <unity-project-directory> --json
```

The checker reports duplicate or malformed GUIDs, likely moves without their `.meta`, orphan or missing `.meta` files, missing script references in text-serialized assets, and a possible mismatch between a script's class and file name. Review each finding against the actual edit: an orphan `.meta` beside a new unrelated asset can resemble a move. A new asset without a `.meta` is an expected warning before import. If the package cache is incomplete, an unresolved script reference is only a warning; restore packages and scan again before concluding that a script is missing.

Treat `class-name-mismatch` as a prompt to inspect the file, not proof that the component cannot load. [Unity 6.3's naming rules](https://docs.unity3d.com/6000.3/Documentation/Manual/naming-scripts.html) allow a mismatched file name when the class is unambiguous, but files defining multiple classes and partial `MonoBehaviour` classes have stricter matching rules. The bundled checker's message uses older, absolute wording; confirm the target Unity version and inspect the classes before deciding whether to rename anything. If a script is already referenced, preserve its `.meta` and serialized references during a rename.

The checker reads selected YAML assets and `MonoScript` references; it does not inspect binary-serialized assets or prove that scripts compile and bind correctly. If the Editor is available, verify import, compilation, and the affected scene or prefab afterward. For live missing-script inspection, follow [validation operations](../skills/validation/GUIDE.md) and the [Editor protocol](../EDITOR.md).

The bundled script is copied unchanged from [awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/19d93f97c9c1ea0f8b306e77aa81e0d3e352d3e9/skills/unity/unity-csharp-scripting/scripts) under Apache-2.0; see its [license](gamedev-agent-skills/LICENSE) and [notice](gamedev-agent-skills/NOTICE).
