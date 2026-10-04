# Rendering and publication

Preserve Jekyll routing, layouts, navigation, aggregation and content-import
contracts. Inspect `_config.yml`, relevant `_layouts`/`_includes` and
`_data/navigation.yml` before changing rendering. Preserve language/front-matter
and package-specific navigation behavior used by imported pages.

Agent entry/rules must never be published as articles. Keep `AGENTS.md`, `.ai/`,
`content/AGENTS.md` and `content/.ai/` excluded in `_config.yml`; the second pair
covers the Content checkout used by the real Pages workflow. Do not place
workflow tasks or rules in copied package documentation trees.

Do not build or deploy the public site unless requested. Validate configuration,
workflow and local link/layout references statically where practical. If a build
is requested, use the existing Gemfile/Jekyll setup and keep generated `_site`,
caches and build output uncommitted. Never turn a static check into a workflow
dispatch, Pages upload or publication.

The site workflow builds/deploys on a `main` push and accepts explicit manual
dispatch and `content-updated`/`docs-updated` events. A requested source edit
does not authorize triggering any of them. Public infrastructure changes and
authored content changes require independent review and delivery.
