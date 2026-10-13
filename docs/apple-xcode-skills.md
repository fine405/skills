# Apple Xcode skills for Codex

## Source

This snapshot contains all ten skills exported directly from Xcode 27.1, build
27A9275, on 2026-10-13. It does not come from a community mirror or OpenAI's
Build iOS Apps plugin. Apple documents export for use with other coding tools in
[Modernize your UIKit app](https://developer.apple.com/videos/play/wwdc2026/278/).

Each independently installable directory contains:

- `SKILL.md`: concise Codex entry point and compatibility workflow.
- `agents/openai.yaml`: Codex display metadata and explicit invocation prompt.
- `apple/guide.md`: exported Apple entry point, renamed to avoid duplicate discovery.
- `apple/references/` and `apple/scripts/`: exported resources, where provided.
- `UPSTREAM.json`: Xcode version/build, export date, original SHA-256 for every file,
  and `packaged_sha256` plus an explanation for an adapted file.
- `UPSTREAM_NOTICE.md`: attribution and the Apple-content license boundary.

Apple files are not relicensed under this repository's MIT License. No separate
upstream license file was included in this export.

## Use in Codex

Install one skill globally with the skills CLI, targeting Codex:

```sh
npx skills add fine405/skills --global --agent codex --skill swiftui-specialist
```

Then ask: "Use $swiftui-specialist to review this feature's view structure and
Observation ownership. Preserve the project's deployment target and architecture."
Use `modernize-tests` for test migrations, and the `whats-new-27` skills only when
the task involves those APIs. Keep XCUITest and XCTest performance tests where
Swift Testing does not replace them.

The entry point reads Apple's bundled guide and follows its references on demand.
Relative upstream paths resolve inside `apple/`, not the repository root. The
security-settings helper keeps its original script/reference directory relationship.
No skill depends on another installed skill or on a local Xcode export path.

These skills do not install MCP servers or grant access to Xcode. In particular,
`device-interaction` requires Apple's DeviceInteraction tools and a usable device
or simulator. If those capabilities are absent, the agent must report that the
workflow cannot run. Other skills can provide code guidance without those tools;
actual builds, previews, security-setting extraction, and device validation still
require the capabilities named by their workflow. API/tool examples are source
guidance, not proof that an operation succeeded.

The Xcode-internal Codex environment is separate from the Codex desktop app. Apple's
release-note workaround using `~/Library/Developer/Xcode/CodingAssistant/codex`
does not install skills into the standalone desktop app.

## Refresh the snapshot

Export into a new staging directory outside the repository. Select the intended
Xcode installation for this command only if it differs from the active toolchain:

```sh
DEVELOPER_DIR=/path/to/Xcode.app/Contents/Developer xcodebuild -version
DEVELOPER_DIR=/path/to/Xcode.app/Contents/Developer \
  xcrun agent skills export --output-dir /tmp/apple-xcode-skills-new
```

Review the exported names and changes before replacing any packaged skill. Copy
all resources into that skill's `apple/` directory, rename the exported `SKILL.md`
to `guide.md`, and retarget any Markdown links to it. Never leave a nested
`SKILL.md`: Codex discovers it as a second skill even when the skills CLI does not.
Refresh `UPSTREAM.json` mappings/hashes and notice; keep `sha256` as the original
export digest and record `packaged_sha256` for any link-adapted file. Preserve
the Codex adapter unless upstream changes require it to change. Update both README
inventories for additions/removals, run the repository gates in `AGENTS.md`, and
verify every packaged upstream file against the export. Updates are manual, not
a background synchronization service.

## Validation boundary

Packaging checks establish metadata, discovery, links, and upstream file integrity.
They do not establish that every Apple API example compiles against a user's SDK,
or that live device, profiling, or migration workflows have been exercised.

Upstream formatting, including existing trailing whitespace, is preserved for
provenance. Only the recorded relative link adjustment changes upstream content.
Whitespace checks for the Codex integration exclude
`skills/apple-platform/*/apple/**`; repository metadata and link checks still
cover the packaged guides.
