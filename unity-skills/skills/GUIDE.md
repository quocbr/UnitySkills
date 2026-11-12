---
name: unity-skills-index
description: Index of all Unity Skills modules with per-module mode labels (SA/FA/Mixed). Use to find which module covers a task before loading its doc.
---

# Unity Skills: Module Index

Module docs. Start with [../SKILL.md](../EDITOR.md) for mode switching and schema-first rules.

> **Multi-instance**: For version-specific projects, call `unity_skills.set_unity_version(...)` first.
> **Schema-first**: Exact signatures come from `GET /skills/recommend?intent=<words>&includeSchema=true&topN=3&wire=v2` (`unity_skills.find_skills(intent, top_n=3, include_schema=True, wire="v2")`) or from `GET /skills/schema?names=a,b&wire=v2` when the name is known. The full `GET /skills/schema` is about 707 KB. Module docs add workflow guidance and guardrails.
> **Split modules**: gameobject, component, batch, script, material, editor, cinemachine, particle, workflow, addressables, asset, behavior, camera, event, light, prefab, qframework, terrain, ui keep shared rules and the skill list in `SKILL.md`, and each skill's parameter table, item fields and return shape in `reference/<skill_name>.md` (one small file per skill). Read the reference file only when the schema's parameter notes are not enough.

## REST modules

Mode labels are guidance only: `SA` means the module's skills mostly run directly in all three modes; `FA` means they mostly need a user grant under Approval; `Mixed` means check the per-skill `mode`; a trailing `*` means the module has auto-forbidden skills (Delete, Play Mode, Domain Reload, high risk). The authoritative per-skill mode is in `GET /skills?full=1`, or `GET /skills/schema?category=<Category>`. Bare `GET /skills` is the brief directory and carries no `mode`.

| Module | Mode | Description | Batch Support |
|--------|:----:|-------------|---------------|
| [gameobject](gameobject/GUIDE.md) | FA* | Object create/move/parent | Yes |
| [component](component/GUIDE.md) | Mixed* | Component add/remove/configure | Yes |
| [material](material/GUIDE.md) | FA | Material property edits | Yes |
| [light](light/GUIDE.md) | FA | Light create/configure | Yes |
| [particle](particle/GUIDE.md) | Mixed | Built-in ParticleSystem (Shuriken) create/configure: typed module patches, renderer, bursts, sub emitters, static diagnosis (not VFX Graph) | Yes |
| [prefab](prefab/GUIDE.md) | Mixed* | Prefab create/apply/spawn, asset queries, component/node edits and atomic batches | Yes |
| [asset](asset/GUIDE.md) | SA* | Asset refresh/find/info | Yes |
| [batch](batch/GUIDE.md) | SA | Batch and async jobs | Built-in |
| [ui](ui/GUIDE.md) | FA | UGUI Canvas/UI creation | Yes |
| [uitoolkit](uitoolkit/GUIDE.md) | Mixed* | UXML/USS/UIDocument | No |
| [script](script/GUIDE.md) | SA* | Script create/read/update | Yes |
| [scene](scene/GUIDE.md) | SA* | Scene load/save/query | No |
| [editor](editor/GUIDE.md) | SA* | Play/select/undo/redo/change journal | No |
| [animator](animator/GUIDE.md) | FA | Animator controllers | No |
| [shader](shader/GUIDE.md) | Mixed* | Shader create/list | No |
| [shadergraph](shadergraph/GUIDE.md) | Mixed* | Shader Graph create/inspect/blackboard edit/constrained node editing | No |
| [graphics](graphics/GUIDE.md) | Mixed | GraphicsSettings / QualitySettings / SRP assets | No |
| [volume](volume/GUIDE.md) | Mixed* | Volume / VolumeProfile / VolumeComponent | No |
| [postprocess](postprocess/GUIDE.md) | FA* | Modern URP/HDRP post-processing | No |
| [urp](urp/GUIDE.md) | Mixed* | URP asset / renderer / renderer features | No |
| [decal](decal/GUIDE.md) | Mixed* | URP Decal Projector workflow | Yes |
| [console](console/GUIDE.md) | SA | Log capture/filter | No |
| [validation](validation/GUIDE.md) | SA* | Broken reference checks | No |
| [importer](importer/GUIDE.md) | Mixed | Texture/audio/model import | Yes |
| [cinemachine](cinemachine/GUIDE.md) | FA* | VCam operations | No |
| [probuilder](probuilder/GUIDE.md) | FA* | ProBuilder mesh edits | No |
| [xr](xr/GUIDE.md) | FA | XRI setup | No |
| [terrain](terrain/GUIDE.md) | FA | Terrain create/paint | No |
| [physics](physics/GUIDE.md) | Mixed | Raycast/overlap/gravity | No |
| [navmesh](navmesh/GUIDE.md) | Mixed* | NavMesh bake/query | No |
| [timeline](timeline/GUIDE.md) | FA* | Timeline tracks/clips | No |
| [workflow](workflow/GUIDE.md) | SA* | Task snapshots/undo, batch orchestration | No |
| [cleaner](cleaner/GUIDE.md) | SA* | Unused/duplicate assets | No |
| [smart](smart/GUIDE.md) | FA* | Query/layout/auto-bind | No |
| [perception](perception/GUIDE.md) | SA | Scene/project analysis | No |
| [camera](camera/GUIDE.md) | FA | Scene View camera | No |
| [event](event/GUIDE.md) | Mixed* | UnityEvent wiring | No |
| [package](package/GUIDE.md) | Mixed* | UPM install/query | No |
| [project](project/GUIDE.md) | SA* | Project info/settings | No |
| [profiler](profiler/GUIDE.md) | SA | Perf statistics | No |
| [optimization](optimization/GUIDE.md) | Mixed | Asset optimization | No |
| [sample](sample/GUIDE.md) | Mixed* | Demo/test skills | No |
| [debug](debug/GUIDE.md) | SA* | Compile/system diagnostics | No |
| [test](test/GUIDE.md) | Mixed* | Unity Test Runner | No |
| [bookmark](bookmark/GUIDE.md) | SA | Scene View bookmarks | No |
| [history](history/GUIDE.md) | SA | Undo/redo history | No |
| [scriptableobject](scriptableobject/GUIDE.md) | Mixed* | ScriptableObject assets | No |
| [netcode](netcode/GUIDE.md) | Mixed* | Netcode for GameObjects setup, prefabs, lifecycle, host/server/client | Yes |
| [addressables](addressables/GUIDE.md) | Mixed* | Addressables authoring: group CRUD, asset entry assignment, profile switching, content build (com.unity.addressables, reflection-based) | No |
| [yooasset](yooasset/GUIDE.md) | Mixed* | YooAsset 2.3.15+ / 3.0.4+ hot-update: build bundles, Collector CRUD, BuildReport asset/dependency analysis, PlayMode runtime validation, Reporter/Debugger tools, AssetArtScanner (2.x only) | Yes |
| [dotween](dotween/GUIDE.md) | Mixed* | DOTween Pro DOTweenAnimation editor-time configuration (add/batch/stagger/tune) | Yes |
| [primetween](primetween/GUIDE.md) | Mixed* | PrimeTween Free inspection, factory discovery, and runtime tween/sequence script generation | No |
| [behavior](behavior/GUIDE.md) | Mixed | Unity Behavior graph assets, agents, blackboard variables (com.unity.behavior, reflection-based) | Yes |
| [hybridclr](hybridclr/GUIDE.md) | Mixed* | HybridCLR hot-update settings, codegen, DLL compile/copy pipeline (com.code-philosophy.hybridclr, reflection-based) | Yes |
| [qframework](qframework/GUIDE.md) | Mixed* | QFramework editor automation: architecture-layer codegen, ViewController/UIKit panel codegen, ResKit AssetBundle mark/build, architecture scan, API doc query (no UPM package, reflection-based) | Yes |

## Advisory modules

Documentation only. These modules define no REST skills. Each description matches the first lines of its doc.

Official Unity manual URLs for a topic, to fetch or hand to the user: [references](../references/README.md). Grep one `##` section; never read a whole index file.

| Module | Description |
|--------|-------------|
| [project-scout](project-scout/GUIDE.md) | Reconnoiter an existing Unity project (version, packages, asmdef, folders, conventions) before proposing changes. |
| [architecture](architecture/GUIDE.md) | Gameplay and system architecture advice: module boundaries, scene/bootstrap layering, data ownership, execution order and update guards. |
| [adr](adr/GUIDE.md) | Record a Unity architecture decision (ADR) with options, rationale and revisit triggers. |
| [performance](performance/GUIDE.md) | High-signal review of Unity performance red flags: Update cadence, hot-path lookups, allocations, pooling, hidden runtime costs. |
| [asmdef](asmdef/GUIDE.md) | Advise on Unity assembly definitions (asmdef): module boundaries, compile speed, editor/runtime/test split. |
| [blueprints](blueprints/GUIDE.md) | Starter architecture blueprints for small games (platformer, shooter, runner, puzzle, tower defense, clicker, card). |
| [script-roles](script-roles/GUIDE.md) | Decide a class's role (MonoBehaviour, ScriptableObject, plain C# service, presenter, installer) before generating scripts. |
| [scene-contracts](scene-contracts/GUIDE.md) | Define explicit Unity scene composition contracts: required objects, component dependencies, bootstrap and reference wiring. |
| [testability](testability/GUIDE.md) | Decide what logic leaves MonoBehaviour for pure C# seams, and plan EditMode vs PlayMode tests. |
| [patterns](patterns/GUIDE.md) | Choose among ScriptableObject, events, interfaces, state machine, object pool and service-layer designs; justify each pattern against simpler options. |
| [async](async/GUIDE.md) | Choose among Update, coroutines, UniTask and timers for runtime work; define cleanup and cancellation ownership. |
| [inspector](inspector/GUIDE.md) | Design Inspector authoring UX: SerializeField exposure, Header/Tooltip organization, validation and attributes. |
| [scriptdesign](scriptdesign/GUIDE.md) | Design review of gameplay scripts: responsibility, role choice, coupling, lifecycle, field ownership (authoring, composition, runtime-mutable), testability. |
| [netcode-design](netcode-design/GUIDE.md) | Source-anchored design rules for Netcode for GameObjects 2.x. |
| [yooasset-design](yooasset-design/GUIDE.md) | Source-anchored design rules for YooAsset v2.3.18, with a 3.x delta sheet. |
| [addressables-design](addressables-design/GUIDE.md) | Source-anchored design rules for Unity Addressables 1.22.3/2.9.1. |
| [unitask-design](unitask-design/GUIDE.md) | Source-anchored design rules for UniTask 2.5.10–2.5.11: PlayerLoop timing, cancellation, composition, conversion, async enumerables, triggers and pitfalls. |
| [dotween-design](dotween-design/GUIDE.md) | Source-anchored design rules for DOTween 1.3.015: tween lifetime, Safe Mode, Sequences, shortcuts, Ease and UniTask bridging. |
| [primetween-design](primetween-design/GUIDE.md) | Source-anchored design rules for PrimeTween 1.4.6: factories, handles, sequences, callbacks, lifetime and integration. |
| [shadergraph-design](shadergraph-design/GUIDE.md) | Source-anchored Shader Graph design rules for Unity 2022.3 and Unity 6 (ShaderGraph 14.0.12 / Unity 6 Graphics package). |
| [pico-design](pico-design/GUIDE.md) | Doc-anchored design rules for PICO Unity Integration SDK v3.4.0 — XR/MR/platform services, version diffs 2.x-3.4, hallucination shields. |
| [qframework-design](qframework-design/GUIDE.md) | Source-anchored design rules for QFramework v1.0.257 — layers, CQRS, BindableProperty, UIKit/ResKit/ActionKit, pitfalls. |
| [yaml-editing](yaml-editing/GUIDE.md) | Last-resort guidance for safely hand-editing Unity YAML. |
| [unity-cli](unity-cli/GUIDE.md) | Experimental Unity CLI on the bound project (opt-in via Library/UnitySkills/cli_config.json): cold start with the Editor closed, headless test, run and build, exit codes, JSON contract, and the allowlist. |
| [manual-gameobject](manual-gameobject/GUIDE.md) | Manually create GameObjects, organize the Hierarchy, and adjust Transforms using Unity Editor UI. For clicks-and-drag workflows that do not need REST automation. |
| [manual-component](manual-component/GUIDE.md) | Manually add, configure, reorder, and copy components on GameObjects using Unity Editor UI. For one-off Inspector workflows that do not need REST automation. |
| [manual-material](manual-material/GUIDE.md) | Manually create and edit Materials and assign them to objects using Unity Editor UI. For one-off material tweaks that do not need REST automation. |
| [manual-scene](manual-scene/GUIDE.md) | Manually navigate, save, and manage scenes using Unity Editor UI. For simple Scene view workflows that do not need REST automation. |
| [skill-creator](skill-creator/GUIDE.md) | Guide for authoring user-defined custom UnitySkills skills inside your own Unity project - a [UnitySkill] C# method plus the conventions that let agents and the server discover and gate it. |
| [evaluation](evaluation/GUIDE.md) | Run the UnitySkills evaluation set (scored benchmark tasks) on the user's own Unity project. Use only when the user explicitly asks to run, resume or continue a UnitySkills evaluation, or pastes an evaluation session prompt; never for ordinary Unity work. |

## Batch-First Rule

When a task touches `2+` objects in Auto / Bypass mode (or after a successful grant under Approval), prefer `*_batch` skills over repeated single-item calls.

## Skill Naming Convention

Skills follow `<module>_<action>` or `<module>_<action>_batch`. Use the schema to verify the exact prefix list.
Special: `scene_analyze`, `hierarchy_describe`, `project_stack_detect` belong to `perception`; `job_*` belongs to `batch`.
If a skill name does not match a valid prefix or a schema result, do not invent it.
