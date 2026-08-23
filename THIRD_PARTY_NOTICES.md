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
