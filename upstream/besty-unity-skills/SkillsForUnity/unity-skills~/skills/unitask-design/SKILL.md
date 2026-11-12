---
name: unity-unitask-design
description: Source-anchored design rules for UniTask 2.5.10 and 2.5.11
---

# UniTask - Design Rules

Advisory module. The source anchors below were checked against Cysharp UniTask **2.5.10** and have not been re-audited against 2.5.11. The [2.5.11 release](https://github.com/Cysharp/UniTask/releases/tag/2.5.11) lists a Unity 6.2+ Editor TreeView compatibility fix and does not list a runtime API change. Use this guide with `com.cysharp.unitask@2.5.10` or `@2.5.11`, after checking the target project's resolved package version.

Each rule cites a concrete file/line so the reasoning is auditable and the AI does not improvise against stale memory.

## When to use

Load before writing or reviewing any of:

- Any `async UniTask` / `async UniTask<T>` / `async UniTaskVoid` method signature
- `.Forget()`, `.AttachExternalCancellation(token)`, `.SuppressCancellationThrow()` chaining
- `UniTask.Yield`, `UniTask.NextFrame`, `UniTask.Delay`, `UniTask.WaitForEndOfFrame`, `UniTask.WaitForFixedUpdate`
- `UniTask.WaitUntil`, `UniTask.WaitWhile`, `UniTask.WaitUntilValueChanged`, `UniTask.WaitUntilCanceled`
- `UniTask.WhenAll`, `UniTask.WhenAny`, `UniTask.WhenEach`
- `UniTask.SwitchToMainThread`, `UniTask.SwitchToThreadPool`, `UniTask.Run`
- `AsyncOperation.ToUniTask()`, `UnityWebRequest.SendWebRequest().ToUniTask()`, `Coroutine.ToUniTask()`
- `this.GetCancellationTokenOnDestroy()`, `GetAsyncStartTrigger()` and other `AsyncTrigger*` extensions
- `UniTaskCompletionSource` / `UniTaskCompletionSource<T>` manual completion sources
- `IUniTaskAsyncEnumerable<T>` / `UniTaskAsyncEnumerable` / `AsyncReactiveProperty<T>` / `Channel<T>`
- WebGL-specific async code paths where `Task.Run` / `SwitchToThreadPool` are forbidden

## Critical Rule Summary

| # | Rule | Source anchor |
|---|------|---------------|
| 1 | `UniTask` is a `readonly partial struct` (value type). Once awaited, its `IUniTaskSource` is recycled; awaiting the same `UniTask` variable twice throws. Use `.Preserve()` to obtain a memoized copy that can be awaited multiple times. | `UniTask.cs:34`, `UniTask.cs:103-113` |
| 2 | A `UniTask` returned by a method must be either `await`ed, `.Forget()`ed, or `.AttachExternalCancellation(token)`ed. Orphan UniTasks silently swallow exceptions into `UniTaskScheduler.UnobservedTaskException`. | `UniTaskScheduler.cs:13`, `UniTaskVoid.cs:11-17` |
| 3 | `PlayerLoopTiming` defines **16** timing slots (2020.2+; **14** on older Unity). Default `UniTask.Yield()` / `UniTask.Delay` uses `PlayerLoopTiming.Update`. Mixing `LastPostLateUpdate` with legacy `WaitForEndOfFrame` coroutines changes observed frame ordering. | `PlayerLoopHelper.cs:71-99` |
| 4 | `UniTask.Delay(int ms, DelayType, PlayerLoopTiming, CancellationToken, bool cancelImmediately)` accepts `DelayType.DeltaTime / UnscaledDeltaTime / Realtime`. The old `bool ignoreTimeScale` overload still exists but mixes semantics — prefer the `DelayType` overload for new code. | `UniTask.Delay.cs:12-20`, `UniTask.Delay.cs:147-165` |
| 5 | `this.GetCancellationTokenOnDestroy()` is defined for `MonoBehaviour`, `GameObject`, and `Component` in `AsyncTriggerExtensions`. Plain C# classes do NOT receive this extension — they must own a `CancellationTokenSource` explicitly. | `Triggers/AsyncTriggerExtensions.cs:14,22,28` |
| 6 | `UniTask.WhenAll(params UniTask[] tasks)` and the `IEnumerable<UniTask>` overload both exist. Semantically match `Task.WhenAll` but are zero-alloc when tasks are UniTask-native. `WhenAny` returns `(winnerIndex, result)` tuple for `UniTask<T>`. | `UniTask.WhenAll.cs:12,22,31,41`, `UniTask.WhenAny.cs` |
| 7 | `AsyncOperation.ToUniTask(IProgress<float>, PlayerLoopTiming, CancellationToken)` is the canonical adapter. `await operation` works too but silently leaks the progress callback if you also set `operation.completed += …`. | `UnityAsyncExtensions.cs` |
| 8 | `UniTaskCompletionSource` and `UniTaskCompletionSource<T>` support `TrySetResult` / `TrySetException` / `TrySetCanceled`. Once any of the three succeeds, subsequent calls return `false` — they do not throw. | `UniTaskCompletionSource.cs:573,610,754,792` |
| 9 | `UniTask.SwitchToThreadPool()` and `UniTask.Run(...)` are compile-time available on all platforms BUT throw `NotSupportedException` at runtime on WebGL. Guard with `#if !UNITY_WEBGL || UNITY_EDITOR` or fall back to `UniTask.Yield()`-based cooperative work. | `UniTask.Threading.cs:57` |
| 10 | Returning `async UniTaskVoid` is the fire-and-forget idiom that lets `await` be used INSIDE the method. `async void` methods cannot return `UniTask` — a common compile error when porting from `Task`. | `UniTaskVoid.cs:11-17`, `UniTask.Factory.cs:112-131` |

## Sub-doc Routing

| Sub-doc | When to read |
|---------|--------------|
| [BASICS.md](./BASICS.md) | `UniTask` vs `Task` differences, struct semantics, `UniTaskVoid`, zero-alloc state machine, `AsyncUniTaskMethodBuilder` |
| [PLAYERLOOP.md](./PLAYERLOOP.md) | 16-value `PlayerLoopTiming` table, Yield/NextFrame/Delay/WaitForEndOfFrame/WaitForFixedUpdate, `DelayType`, frame-ordering with legacy coroutines |
| [CANCELLATION.md](./CANCELLATION.md) | `CancellationToken` patterns, `GetCancellationTokenOnDestroy` (3 overloads), `AttachExternalCancellation`, `CancelAfterSlim`, `AddTo`, `OperationCanceledException` flow |
| [COMPOSITION.md](./COMPOSITION.md) | `WhenAll`, `WhenAny`, `WhenEach`, `Forget`, `SuppressCancellationThrow`, `ContinueWith`, timeout patterns |
| [CONVERSION.md](./CONVERSION.md) | `AsyncOperation.ToUniTask`, `UnityWebRequest.SendWebRequest().ToUniTask`, `IEnumerator.ToUniTask`, `Task.AsUniTask`, `UniTask.AsTask`, `UniTask.ToCoroutine` |
| [ASYNCENUMERABLE.md](./ASYNCENUMERABLE.md) | `IUniTaskAsyncEnumerable<T>`, `UniTaskAsyncEnumerable`, `AsyncReactiveProperty<T>`, `Channel<T>`, `EveryValueChanged`, `Publish`, LINQ-to-async operators |
| [TRIGGERS.md](./TRIGGERS.md) | `AsyncTriggerBase`, `GetAsyncStartTrigger`, `GetAsyncDestroyTrigger`, `OnCollisionEnterAsync`, `OnClickAsync`, `MonoBehaviourMessagesTriggers`, lifecycle cancellation |
| [PITFALLS.md](./PITFALLS.md) | 30 concrete hallucination / runtime pitfalls (double-await, forgotten Forget, WebGL threadpool, tracker memory, wrong PlayerLoopTiming, coroutine interop bugs) |

## Routing to Other Modules

- Choice between `UniTask`, raw `Task`, and `IEnumerator` at the architecture layer → load [async](../async/SKILL.md)
- DOTween tween → UniTask adapter (`tween.ToUniTask(TweenCancelBehaviour, token)`) → load [dotween-design](../dotween-design/SKILL.md)
- YooAsset handle → UniTask via `handle.ToUniTask()` extension → load [yooasset-design](../yooasset-design/SKILL.md)
- Addressables `AsyncOperationHandle.ToUniTask()` rules → load [addressables-design](../addressables-design/SKILL.md)
- Performance review of UniTask-heavy code paths (tracker cost, state machine alloc) → load [performance](../performance/SKILL.md)
- Asmdef layout for UniTask consumers (`Cysharp.Threading.Tasks.asmdef` reference) → load [asmdef](../asmdef/SKILL.md)

## Version Scope

Targets **UniTask 2.5.10–2.5.11**. Source line anchors are from 2.5.10; confirm them against 2.5.11 when relying on an implementation detail. Earlier 2.x versions are mostly source-compatible; key differences:
- `WaitForEndOfFrame(MonoBehaviour coroutineRunner)` overload added in recent 2.x — on 2023.1+ a parameterless overload is available (`#if UNITY_2023_1_OR_NEWER`). See `UniTask.Delay.cs:78-103`.
- `UniTask.WhenEach` is a newer addition; not all 2.x builds ship it.

When in doubt, read the cited source — not your memory.
