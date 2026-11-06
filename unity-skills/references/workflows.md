# Unified Unity workflows

Read the section for the requested capability. Official references define Unity APIs and design constraints. Editor references describe the corresponding Besty operations and their limits. All are resources within `unity-skills`.

## UI and text

Identify the framework from explicit requirements or the existing scene and source. Use the [UI framework guide](unity-technologies/ui/GUIDE.md) for ambiguous menus, HUDs and editor panels.

- **UI Toolkit** (`.uxml`, `.uss`, `UIDocument`, `CreateGUI`). Use the [authoring guide](unity-technologies/ui-uitk/GUIDE.md) for layout, controls and runtime bindings. In an open Editor, use [the UI Toolkit operations](../skills/uitoolkit/GUIDE.md) to inspect existing files and documents, then create or update only the needed UXML, USS, `PanelSettings` or document. Verify the assigned visual tree and panel settings and, for runtime UI, verify its binding in the actual panel.
- **uGUI** (`Canvas`, `RectTransform`, prefab UI). Use the [uGUI guide](unity-technologies/ui-ugui/GUIDE.md) to design hierarchy, anchors and layout. Use [the uGUI operations](../skills/ui/GUIDE.md) to inspect and edit scene controls. Use [prefab operations](../skills/prefab/GUIDE.md) when the target is a prefab asset. Verify anchors and parent layout at the target aspect ratios.
- **IMGUI** (`OnGUI`, `OnInspectorGUI`). Follow [the IMGUI guide](unity-technologies/ui-imgui/GUIDE.md) for editor C# code. If updating via the running Editor, use [the script operations](../skills/script/GUIDE.md) and check compilation. uGUI operations apply to Canvas objects and UI Toolkit operations apply to UXML, USS and visual elements.
- For multilingual text or font issues, use [Localization](unity-technologies/localization/GUIDE.md) or [TextMeshPro optimization](unity-technologies/optimize-text-mesh-pro/GUIDE.md) with the applicable UI framework above.

## CLI, Pipeline, tests and builds

Use [the official Unity CLI guide](unity-technologies/unity-cli/GUIDE.md) for Editor and license management, independent CLI tasks, and CI. Check the installed binary's `--version` and relevant `--help` before selecting arguments. Use [the Pipeline guide](unity-technologies/unity-pipeline/GUIDE.md) when the task requires Pipeline commands or a connected Player and the matching package is available.

For Besty-mediated cold start or headless test, run or build, first check the bound project's `Library/UnitySkills/cli_config.json`. Use its `cliPath` and the applicable feature switch as described in [the bound-project CLI reference](../skills/unity-cli/GUIDE.md). Confirm Editor liveness and its project lock before opening or launching a second process. The cold-start marker can start the REST server and belongs only in the opt-in Besty workflow. When the target Editor is already running and REST is available, use [Editor operations](../skills/editor/GUIDE.md) and [Test Runner operations](../skills/test/GUIDE.md) for supported live work. Report actual test/build results from the chosen backend.

For a new game or prototype, use [the project bootstrap guide](unity-technologies/new-unity-project/GUIDE.md). Its delegated Workbench guides are already under `references/unity-technologies/`. Read them in place and skip installing or mirroring separate copies. Use [game polish](unity-technologies/craft-game-floors/GUIDE.md) for a first playable experience and [Web optimization](unity-technologies/optimize-web/GUIDE.md) for WebGL/WebGPU targets.

## Unity Package Manager

Read [the UPM guide](unity-technologies/unity-package-management/GUIDE.md) for package IDs, compatible versions and headless approaches. For an open Editor, use [the package operations](../skills/package/GUIDE.md) to inspect the installed state and dependencies. `package_search` searches the installed cache. Use the official registry discovery workflow when the requested package is absent from that cache.

Choose the headless or live write path according to the Editor state, available tools and permissions. For an open Editor use the supported Besty operation only when allowed by its schema and mode. Wait for any reload and verify both the resolved version and project manifest or lockfile. A blocked REST mutation is handled through its policy flow.

## Navigation and physics

- **NavMesh.** Follow [AI Navigation](unity-technologies/initialize-ai-navigation/GUIDE.md) to choose surfaces, agents, links, and the right package. For a running Editor, use [NavMesh operations](../skills/navmesh/GUIDE.md) for supported bake, agent, obstacle or path work. Verify the agent can query a route on the intended surface with the correct agent type and area mask. Author missing surface/link features with the version-appropriate Unity API.
- **3D collisions and queries.** Use [the PhysX diagnosis guide](unity-technologies/physics-3d-collision/GUIDE.md) to check layers, colliders, Rigidbody and callback setup. Use [physics operations](../skills/physics/GUIDE.md) and [component inspection](../skills/component/GUIDE.md) to check the live scene and run targeted 3D queries. A raycast confirms query behavior. Runtime collision callbacks must be verified in Play Mode when authorized.
- **2D physics.** Select the appropriate system with [2D physics](unity-technologies/create-2d-physics/GUIDE.md). Use component inspection where supported and the chosen system's own API for 2D physics queries and callbacks.

## Rendering, Shader Graph and post-processing

- **URP post-processing.** Use [the URP post-processing guide](unity-technologies/urp-postprocessing/GUIDE.md) to diagnose camera settings, volume layers, profiles, and overrides. Read [the Volume operations](../skills/volume/GUIDE.md) to find the profile and [the effect operations](../skills/postprocess/GUIDE.md) for supported parameters. Confirm whether the profile is shared before editing. Verify override state and the effect in the target camera.
- **URP conversion or Renderer Features.** Use [the migration guide](unity-technologies/migrate-birp-to-urp/GUIDE.md) for Built-in to URP conversion and [the Render Graph review guide](unity-technologies/validate-urp-render-graph-renderer-feature/GUIDE.md) for custom Unity 6 pass code. Use [URP operations](../skills/urp/GUIDE.md) for live asset, renderer and feature inspection or supported wiring. Check the actual pipeline asset and renderer assigned to the target camera.
- **Shader Graph.** Use [the custom HLSL node guide](unity-technologies/shader-graph-create-custom-node/GUIDE.md) for function signatures and node setup. Use [Shader Graph operations](../skills/shadergraph/GUIDE.md) to inspect the graph, blackboard, or perform supported graph edits. Validate graph compilation and material output after the change.
- For custom graph editors use [Graph Toolkit](unity-technologies/build-gtk/GUIDE.md) and check the guide's minimum Unity version. For retro sprite rendering use [2D Pixel Perfect](unity-technologies/2d-pixel-perfect/GUIDE.md).

## Search, assets, and performance

- **Search.** Use [Unity Search](unity-technologies/generate-editor-search-query/GUIDE.md) when building a Search query or opening the Search window. Use [asset](../skills/asset/GUIDE.md), [scene](../skills/scene/GUIDE.md), or [GameObject](../skills/gameobject/GUIDE.md) queries when the agent needs actual project results. Verify the filter and scope before acting on the matches.
- **Import and sprites.** Inspect existing settings through [importer operations](../skills/importer/GUIDE.md). Use [Sprite Editor](unity-technologies/sprite-editor/GUIDE.md) for slicing, pivots or borders, [Sprite Atlas](unity-technologies/manage-sprite-atlas/GUIDE.md) for packing, [sprite structure analysis](unity-technologies/sprite-segment-3x3grid/GUIDE.md) for 3×3 segmentation, and [tile palettes](unity-technologies/create-tile-palette-or-rule-tiles/GUIDE.md) for Tile Palette or Rule Tile authoring. Use [Asset Transformer Toolkit](unity-technologies/asset-transformer-toolkit/GUIDE.md) for its specialized model and point-cloud imports after checking its package requirements.
- **Audio.** Use [Audio Mixer routing](unity-technologies/audio-setup-mixers/GUIDE.md) for source-to-group assignment and [audio optimization](unity-technologies/optimize-audio/GUIDE.md) to select import settings. [Importer](../skills/importer/GUIDE.md) and [optimization](../skills/optimization/GUIDE.md) operations can inspect and apply supported compression changes. Verify the reimported clip settings and the trade-off in its actual playback context.
- **Audits.** Start with the requested metric or symptom. Use [Project Auditor](unity-technologies/project-auditor-fixes/GUIDE.md) for its report and rules. Use [profiler](../skills/profiler/GUIDE.md), [optimization](../skills/optimization/GUIDE.md) or [validation](../skills/validation/GUIDE.md) for supported live measurements and checks. Rerun the same measurement or rule after changes.

## Multiplayer and game services

Use [Multiplayer Services](unity-technologies/setup-multiplayer-services/GUIDE.md) for sessions, matchmaking, lobbies and topology. If Netcode for GameObjects is the selected transport-facing game stack, use [Netcode operations](../skills/netcode/GUIDE.md) for supported scene, prefab and NetworkManager work. Verify the service session and in-game connectivity independently.

- [Vivox](unity-technologies/setup-vivox-voice-chat/GUIDE.md) covers game voice and text chat.
- [Unity Gaming Services](unity-technologies/build-live-game/GUIDE.md) covers authentication, cloud logic, saves, economy and leaderboards.
- [Unity In-App Purchasing](unity-technologies/implement-in-app-purchases/GUIDE.md) and [LevelPlay](unity-technologies/levelplay-unity-integration/GUIDE.md) cover purchases and ads respectively.
