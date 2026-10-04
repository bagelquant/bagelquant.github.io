# Website AI rules

Start with [AGENTS.md](../AGENTS.md). Always read
[Website ownership and imports](rules/website.md); for layout, route, build,
dispatch or deployment work also read [Rendering and publication](rules/rendering.md).

| Work | Local authority |
| --- | --- |
| Source ownership, copied docs, content checkout and provenance | [Website/import rules](rules/website.md) |
| Jekyll routes/layouts, navigation, exclusions and publication | [Rendering rules](rules/rendering.md) |

Local rules are self-contained. Add the workspace workflow only after verifying
a workspace as described in the entry point. A standalone site
checkout does not require the workspace CLI and creates no `.ai/tasks/`.

Check changed configuration, relative destinations, navigation and layout
references against the actual source files. For import changes, inspect
`.github/workflows/jekyll.yml` and `scripts/source_revisions.py`. Keep static
validation separate from a requested Jekyll build or live deployment. Do not
generate `_site` merely to validate agent instructions.
