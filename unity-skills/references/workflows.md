# Unified Unity workflows

Read the section for the requested capability. Official references define Unity workflows and design constraints. Nice Wolf Studio's Unity 6.3 references provide code patterns and review cases. Besty references describe live Editor operations. Check the project's actual Unity and package versions before applying examples. Use the Workbench routing and permissions for execution.

## C# implementation and code review

Use [scripting](nice-wolf-studio/unity-scripting/GUIDE.md) and [Unity foundations](nice-wolf-studio/unity-foundations/GUIDE.md) to choose the Unity APIs and object model. For review, start from the failing behavior and relevant code path. Check [lifecycle](nice-wolf-studio/unity-lifecycle/GUIDE.md) for object lifetime, initialization and scene transitions, [async patterns](nice-wolf-studio/unity-async-patterns/GUIDE.md) for cancellation and cleanup, and [3D math](nice-wolf-studio/unity-3d-math/GUIDE.md) for space conversions, rotation or projection errors. Report review findings with file locations and observed consequences. Use [the script operations](../skills/script/GUIDE.md) when a requested Editor action needs them.

For custom authoring tools, use [Editor tooling patterns](nice-wolf-studio/unity-editor-tools/GUIDE.md) for inspectors, serialization, Gizmos, and EditorWindows. Choose the UI framework below before writing the visual layer.

## Gameplay architecture and content design

- Use [game architecture](nice-wolf-studio/unity-game-architecture/GUIDE.md) and [state machines](nice-wolf-studio/unity-state-machines/GUIDE.md) to decide ownership, transitions and test boundaries. Use [game loops](nice-wolf-studio/unity-game-loop/GUIDE.md) to specify session flow, win/loss, progression and pacing.
- Use [data-driven design](nice-wolf-studio/unity-data-driven/GUIDE.md) to separate authoring data from runtime state and [save systems](nice-wolf-studio/unity-save-system/GUIDE.md) for persistence, migration and recovery. For scene transitions and Addressables lifetimes, use [scenes and asset loading](nice-wolf-studio/unity-scene-assets/GUIDE.md) with [the Addressables operations](../skills/addressables/GUIDE.md).
- Use [NPC behavior](nice-wolf-studio/unity-npc-behavior/GUIDE.md) for perception and decisions, [level design](nice-wolf-studio/unity-level-design/GUIDE.md) for encounters and checkpoints, and [procedural generation](nice-wolf-studio/unity-procedural-gen/GUIDE.md) for seeded content and generation constraints. Use the live Editor only for requested inspection or supported authoring after choosing the design.

## Input and ECS/DOTS

- Identify the input backend before editing. Use [Input System](nice-wolf-studio/unity-input/GUIDE.md) to implement actions, devices and rebinding. Use [input correctness](nice-wolf-studio/unity-input-correctness/GUIDE.md) to review control schemes, action phases, rebinding persistence and local multiplayer devices.
- Use [ECS/DOTS](nice-wolf-studio/unity-ecs-dots/GUIDE.md) for Entities, Jobs, Burst, baking and SubScenes. Check the installed package versions and distinguish Entities workflows from GameObject authoring before selecting an API.

## UI and text

Identify the framework from explicit requirements or the existing scene and source. Use the [UI framework guide](unity-technologies/ui/GUIDE.md) for ambiguous menus, HUDs and editor panels.
Use [UI patterns](nice-wolf-studio/unity-ui-patterns/GUIDE.md) for screen flow, dynamic lists, HUD state or transitions and [Unity 6.3 UI examples](nice-wolf-studio/unity-ui/GUIDE.md) for implementation details after choosing the framework.

- **UI Toolkit** (`.uxml`, `.uss`, `UIDocument`, `CreateGUI`). Use the [authoring guide](unity-technologies/ui-uitk/GUIDE.md) for layout, controls and runtime bindings. In an open Editor, use [the UI Toolkit operations](../skills/uitoolkit/GUIDE.md) to inspect existing files and documents, then create or update only the needed UXML, USS, `PanelSettings` or document. Verify the assigned visual tree and panel settings and, for runtime UI, verify its binding in the actual panel.
- **uGUI** (`Canvas`, `RectTransform`, prefab UI). Use the [uGUI guide](unity-technologies/ui-ugui/GUIDE.md) to design hierarchy, anchors and layout. Use [the uGUI operations](../skills/ui/GUIDE.md) to inspect and edit scene controls. Use [prefab operations](../skills/prefab/GUIDE.md) when the target is a prefab asset. Verify anchors and parent layout at the target aspect ratios.
- **IMGUI** (`OnGUI`, `OnInspectorGUI`). Follow [the IMGUI guide](unity-technologies/ui-imgui/GUIDE.md) for editor C# code. If updating via the running Editor, use [the script operations](../skills/script/GUIDE.md) and check compilation. uGUI operations apply to Canvas objects and UI Toolkit operations apply to UXML, USS and visual elements.
- For multilingual text or font issues, use [Localization](unity-technologies/localization/GUIDE.md) or [TextMeshPro optimization](unity-technologies/optimize-text-mesh-pro/GUIDE.md) with the applicable UI framework above.

## CLI, Pipeline, tests and builds

Use [the official Unity CLI guide](unity-technologies/unity-cli/GUIDE.md) for Editor and license management, independent CLI tasks, and CI. Check the installed binary's `--version` and relevant `--help` before selecting arguments. Use [the Pipeline guide](unity-technologies/unity-pipeline/GUIDE.md) when the task requires Pipeline commands or a connected Player and the matching package is available.

Use [test patterns](nice-wolf-studio/unity-testing/GUIDE.md) to choose Edit Mode or Play Mode and make the regression observable. Use [platform builds](nice-wolf-studio/unity-platforms/GUIDE.md) for Build Profiles, platform defines, mobile targets and IL2CPP. When an installed CLI command behaves differently from its reference, consult the [CLI contract](nice-wolf-studio/unity-cli-contract/GUIDE.md) and [surface preflight](nice-wolf-studio/unity-surface-preflight/GUIDE.md) for diagnostic ideas. Use the Workbench's own CLI and Editor protocol above for execution, dependency setup, and permission decisions. Treat the upstream CLI examples as versioned observations.

For Besty-mediated cold start or headless test, run or build, first check the bound project's `Library/UnitySkills/cli_config.json`. Use its `cliPath` and the applicable feature switch as described in [the bound-project CLI reference](../skills/unity-cli/GUIDE.md). Confirm Editor liveness and its project lock before opening or launching a second process. The cold-start marker can start the REST server and belongs only in the opt-in Besty workflow. When the target Editor is already running and REST is available, use [Editor operations](../skills/editor/GUIDE.md) and [Test Runner operations](../skills/test/GUIDE.md) for supported live work. Report actual test/build results from the chosen backend.

For a new game or prototype, use [the project bootstrap guide](unity-technologies/new-unity-project/GUIDE.md). Its delegated Workbench guides are already under `references/unity-technologies/`. Read them in place and skip installing or mirroring separate copies. Use [game polish](unity-technologies/craft-game-floors/GUIDE.md) for a first playable experience and [Web optimization](unity-technologies/optimize-web/GUIDE.md) for WebGL/WebGPU targets.

## Unity Package Manager

Read [the UPM guide](unity-technologies/unity-package-management/GUIDE.md) for package IDs, compatible versions and headless approaches. For an open Editor, use [the package operations](../skills/package/GUIDE.md) to inspect the installed state and dependencies. `package_search` searches the installed cache. Use the official registry discovery workflow when the requested package is absent from that cache.
Use [package and services examples](nice-wolf-studio/unity-packages-services/GUIDE.md) for project integration and use the project's resolved package versions for API details.

Choose the headless or live write path according to the Editor state, available tools and permissions. For an open Editor use the supported Besty operation only when allowed by its schema and mode. Wait for any reload and verify both the resolved version and project manifest or lockfile. A blocked REST mutation is handled through its policy flow.

## Navigation and physics

- **NavMesh.** Follow [AI Navigation](unity-technologies/initialize-ai-navigation/GUIDE.md) to choose surfaces, agents, links, and the right package. For a running Editor, use [NavMesh operations](../skills/navmesh/GUIDE.md) for supported bake, agent, obstacle or path work. Verify the agent can query a route on the intended surface with the correct agent type and area mask. Author missing surface/link features with the version-appropriate Unity API.
- **3D collisions and queries.** Use [the PhysX diagnosis guide](unity-technologies/physics-3d-collision/GUIDE.md) to check layers, colliders, Rigidbody and callback setup. Use [physics operations](../skills/physics/GUIDE.md) and [component inspection](../skills/component/GUIDE.md) to check the live scene and run targeted 3D queries. A raycast confirms query behavior. Runtime collision callbacks must be verified in Play Mode when authorized.
- **2D physics.** Select the appropriate system with [2D physics](unity-technologies/create-2d-physics/GUIDE.md). Use component inspection where supported and the chosen system's own API for 2D physics queries and callbacks.
- Use [physics examples](nice-wolf-studio/unity-physics/GUIDE.md) and [physics query correctness](nice-wolf-studio/unity-physics-queries/GUIDE.md) for movement, query type, hit order, masks and triggers. Use [navigation and inference](nice-wolf-studio/unity-ai-navigation/GUIDE.md) for runtime NavMesh logic and Sentis inference with the corresponding package.

## Rendering, Shader Graph and post-processing

- **URP post-processing.** Use [the URP post-processing guide](unity-technologies/urp-postprocessing/GUIDE.md) to diagnose camera settings, volume layers, profiles, and overrides. Read [the Volume operations](../skills/volume/GUIDE.md) to find the profile and [the effect operations](../skills/postprocess/GUIDE.md) for supported parameters. Confirm whether the profile is shared before editing. Verify override state and the effect in the target camera.
- **URP conversion or Renderer Features.** Use [the migration guide](unity-technologies/migrate-birp-to-urp/GUIDE.md) for Built-in to URP conversion and [the Render Graph review guide](unity-technologies/validate-urp-render-graph-renderer-feature/GUIDE.md) for custom Unity 6 pass code. Use [URP operations](../skills/urp/GUIDE.md) for live asset, renderer and feature inspection or supported wiring. Check the actual pipeline asset and renderer assigned to the target camera.
- **Shader Graph.** Use [the custom HLSL node guide](unity-technologies/shader-graph-create-custom-node/GUIDE.md) for function signatures and node setup. Use [Shader Graph operations](../skills/shadergraph/GUIDE.md) to inspect the graph, blackboard, or perform supported graph edits. Validate graph compilation and material output after the change.
- For custom graph editors use [Graph Toolkit](unity-technologies/build-gtk/GUIDE.md) and check the guide's minimum Unity version. For retro sprite rendering use [2D Pixel Perfect](unity-technologies/2d-pixel-perfect/GUIDE.md).
- Use [graphics patterns](nice-wolf-studio/unity-graphics/GUIDE.md) and [lighting and VFX](nice-wolf-studio/unity-lighting-vfx/GUIDE.md) for rendering code, probes, Particle Systems or VFX Graph. For animated behavior or camera transitions, use [animation and Timeline](nice-wolf-studio/unity-animation/GUIDE.md) or [Cinemachine](nice-wolf-studio/unity-cinemachine/GUIDE.md) with the applicable Editor module.

## Search, assets, and performance

- **Search.** Use [Unity Search](unity-technologies/generate-editor-search-query/GUIDE.md) when building a Search query or opening the Search window. Use [asset](../skills/asset/GUIDE.md), [scene](../skills/scene/GUIDE.md), or [GameObject](../skills/gameobject/GUIDE.md) queries when the agent needs actual project results. Verify the filter and scope before acting on the matches.
- **Import and sprites.** Inspect existing settings through [importer operations](../skills/importer/GUIDE.md). Use [Sprite Editor](unity-technologies/sprite-editor/GUIDE.md) for slicing, pivots or borders, [Sprite Atlas](unity-technologies/manage-sprite-atlas/GUIDE.md) for packing, [sprite structure analysis](unity-technologies/sprite-segment-3x3grid/GUIDE.md) for 3×3 segmentation, and [tile palettes](unity-technologies/create-tile-palette-or-rule-tiles/GUIDE.md) for Tile Palette or Rule Tile authoring. Use [Asset Transformer Toolkit](unity-technologies/asset-transformer-toolkit/GUIDE.md) for its specialized model and point-cloud imports after checking its package requirements.
- **Audio.** Use [Audio Mixer routing](unity-technologies/audio-setup-mixers/GUIDE.md) for source-to-group assignment and [audio optimization](unity-technologies/optimize-audio/GUIDE.md) to select import settings. [Importer](../skills/importer/GUIDE.md) and [optimization](../skills/optimization/GUIDE.md) operations can inspect and apply supported compression changes. Verify the reimported clip settings and the trade-off in its actual playback context.
- **Audits.** Start with the requested metric or symptom. Use [Project Auditor](unity-technologies/project-auditor-fixes/GUIDE.md) for its report and rules. Use [profiler](../skills/profiler/GUIDE.md), [optimization](../skills/optimization/GUIDE.md) or [validation](../skills/validation/GUIDE.md) for supported live measurements and checks. Rerun the same measurement or rule after changes.
- Use [2D patterns](nice-wolf-studio/unity-2d/GUIDE.md) for Sprite sorting, Tilemaps or 2D lighting, [audio examples](nice-wolf-studio/unity-audio/GUIDE.md) for spatial playback and routing, and [profiling patterns](nice-wolf-studio/unity-performance/GUIDE.md) to select a measurement before changing an asset or code path.

## Multiplayer and game services

Use [Multiplayer Services](unity-technologies/setup-multiplayer-services/GUIDE.md) for sessions, matchmaking, lobbies and topology. If Netcode for GameObjects is the selected transport-facing game stack, use [Netcode operations](../skills/netcode/GUIDE.md) for supported scene, prefab and NetworkManager work. Verify the service session and in-game connectivity independently.
Use [multiplayer patterns](nice-wolf-studio/unity-multiplayer/GUIDE.md) for ownership, RPCs, NetworkVariables and synchronization. Use [XR patterns](nice-wolf-studio/unity-xr/GUIDE.md) for XR Interaction Toolkit, OpenXR and AR Foundation after checking the target SDK.

- [Vivox](unity-technologies/setup-vivox-voice-chat/GUIDE.md) covers game voice and text chat.
- [Unity Gaming Services](unity-technologies/build-live-game/GUIDE.md) covers authentication, cloud logic, saves, economy and leaderboards.
- [Unity In-App Purchasing](unity-technologies/implement-in-app-purchases/GUIDE.md) and [LevelPlay](unity-technologies/levelplay-unity-integration/GUIDE.md) cover purchases and ads respectively.
