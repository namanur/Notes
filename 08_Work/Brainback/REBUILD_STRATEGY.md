# Brain Back: Rebuild Strategy (The Stoic Curator)

## 1. Objective
A complete architectural and visual overhaul of "Brain Back," transforming it from a utility-first blocker into a sophisticated, editorial-style "Attention Firewall." The rebuild focuses on psychological grounding (The Stoic Curator design system) and data-driven insights (Intercept Velocity, Stability Index).

## 2. Key Files & Context
- **Legacy Logic:** `BlockerService.kt` (Accessibility Hooks), `FrictionManager.kt` (Lock/Break state), `StatsManager.kt` (Usage calculation).
- **Design System:** Stitch "Stoic Curator" — Asymmetric layouts, tonal depth (surface-to-surface hierarchy), and high-contrast editorial typography.
- **Vault Location:** `Notes/08_Work/Brainback/`

## 3. Implementation Steps

### Phase 1: Core Engine Refactoring (The Brain)
- **Domain Layer:** Define `UseCases` for `InterceptApp`, `StartFocusSession`, and `CalculateStabilityIndex`.
- **Data Layer:** 
    - Migrate from `SharedPreferences` to **Room** (`AttentionDatabase`).
    - Schema: `BlockEvents`, `UsageSnapshots`, `FocusSessions`.
- **Service Layer:** 
    - Refactor `BlockerService` into a `ReactiveInterceptor` that broadcasts events to the repository.
    - Implement `HeuristicEngine` to isolate Reels/Shorts/Spotlight logic.

### Phase 2: Analytics & Insights (The Logic)
- **Stability Index:** A composite score (0-100) calculated by:
    - `FocusTime` / (`FocusTime` + `ReactiveAppTime`).
- **Intercept Velocity:** `BlockCount` / `TotalUsageTime`.
- **Attention Fractures:** Count of `MOVE_TO_FOREGROUND` events for "Loop Apps" (IG, Snap, YT).

### Phase 3: Stoic UI Implementation (The Face)
- **Theme:** Implement `StoicTheme` using Compose `Material3` with custom tonal palettes (Surface-to-Surface hierarchy).
- **Screens:**
    1. **Home (Dashboard):** Hero time display, Dopamine Cycle indicator, and Blocked Attempt summary.
    2. **Intercepts:** List of firm boundaries (App-specific block stats).
    3. **Weekly Summary:** Bar charts for Focus vs. Reactive usage, and daily unlock metrics.
    4. **Trends:** Stability Index heatmap and "Morning Clarity" observations.

### Phase 4: Verification & Testing
- **Unit Tests:** `StabilityIndexCalculatorTest`, `HeuristicEngineTest`.
- **Integration Tests:** Verifying Accessibility Service lifecycle and Room persistence.

## 4. Verification & Testing Plan
- **Reproduction:** Verify that the legacy `BlockerService` heuristics still work on target apps (IG Reels, YT Shorts).
- **Performance:** Ensure `UsageStatsManager` queries don't impact UI fluidity (offload to `Dispatchers.IO`).
- **UX Audit:** Validate the "No-Line" rule (boundaries defined by tonal shifts, not borders).
