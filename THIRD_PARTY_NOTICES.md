# Third-party notices

## Hallmark

The `hallmark-build`, `hallmark-audit`, and `hallmark-study` skills are adapted
from [Nutlope/hallmark](https://github.com/Nutlope/hallmark) commit
`13ac0ec7e148655948100b6396439e481361d690`.

Upstream Hallmark is available under the MIT License. A copy of its copyright
and permission notice is included as `UPSTREAM_LICENSE` inside each adapted
skill so it remains present when a skill is installed independently.

The adaptations split the original modes, reduce mandatory context, remove
automatic project-memory and token-file side effects, separate planning from
post-build verification, and add deterministic static checks without claiming
they replace rendered or accessibility testing.

## Design Direction

The `design-direction` skill is inspired by Anshu Chimala’s article
“How to turn your AI into a world-class designer,” published in Lenny’s
Newsletter. It independently expresses the Discover–Define–Deliver workflow
with bounded screenshot critique and optional generated media. The article
and its illustrations are not distributed with this repository; no license
to those source materials is implied by the repository’s MIT License.

## Write Explain

The `write-explain` skill contains original workflow instructions informed by
[ASD-STE100](https://www.asd-ste100.org/faq.html),
[Ruanyf’s Chinese technical-document writing guide](https://github.com/ruanyf/document-style-guide),
[Chinese Copywriting Guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines),
and [Microsoft’s localization style guides](https://learn.microsoft.com/zh-cn/globalization/reference/microsoft-style-guides).
Its references identify these sources and distinguish user style preferences
from source guidance. The source manuals and controlled dictionaries are not
redistributed, and the skill does not claim ASD-STE100 compliance.

## Apple Xcode skills

The ten skills in `skills/apple-platform/` package Apple-authored guidance exported
from Xcode 27.1 (build 27A9275) on 2026-10-13. Each skill keeps all exported files
under `apple/`, with the upstream entry point renamed to `guide.md` to avoid
duplicate discovery. A relative entry-point link is adjusted where recorded.
The outer Codex entry point is the only installable skill. Its `UPSTREAM.json` records paths and SHA-256
hashes, and its `UPSTREAM_NOTICE.md` travels with independent installations.

The export contains no standalone license file. This repository's MIT License
does not apply to Apple's files; no additional rights to Apple's content are
granted. Codex entry points and metadata are original integration material.
See [export, compatibility, and update notes](./docs/apple-xcode-skills.md).
