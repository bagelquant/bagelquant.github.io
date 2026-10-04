# Website agent entry point

This repository owns Jekyll rendering, routes/navigation, themes/assets,
aggregation and Pages deployment. Authored content and package/application
documentation remain in their source repositories.

## Start every task

1. Read [.ai/README.md](.ai/README.md) and its local rules, then
   [README.md](README.md), [Gemfile](Gemfile), [_config.yml](_config.yml) and the
   relevant layout/navigation/workflow. Inspect tracked and untracked Git
   status before editing. These local rules work in a standalone checkout.
2. Resolve the owner with `git rev-parse --show-toplevel` and a workspace
   candidate with `git rev-parse --show-superproject-working-tree`; if empty,
   check ancestors. Accept only a candidate whose `.gitmodules` registers the
   owner's exact relative path, Git index has mode `160000` there and owner
   Git root matches that path. Require `.ai/README.md`, `.ai/workflow.md` and
   `scripts/ai.py`, then follow the root's full discovery validation. Read its
   `AGENTS.md`/`.ai/README.md`; records stay only in its `.ai/tasks/`. Names and
   arbitrary `../` paths are not proof. Standalone work creates no local task
   archive and uses conversation progress/handoff.

## Working boundaries

- Edit articles/public App landing pages in `bagelquant-content`, Core/Data/BT
  docs in their packages and application docs in Workbench. Never manually
  edit generated/copied `content/` or `_site`.
- Keep the actual collection boundary: default branches from GitHub Content
  and Core/Data/BT docs; no workspace gitlink pins or Workbench docs.
- Preserve Jekyll routing, layouts, navigation and import contracts. Keep agent
  instructions and `.ai/` excluded from the public build, including beneath
  the workflow's `content/` checkout.
- Preserve unrelated work and Git metadata. Do not alter shared numerical data,
  credentials, local environments or package caches as cleanup.
- Prefer small coherent changes and existing tools; avoid duplicate source
  paths, new dependencies or compatibility layers without a concrete need.
- Do not build or deploy the public site unless requested. No commit, push,
  PR, merge, publish, dispatch, service installation, provider/data operation
  or governance transition without a specific request. Pushes to `main`
  trigger Pages; task records do not authorize external actions.
- Keep `main` stable and branches short-lived; default agent branches use
  `codex/` unless instructed otherwise. Requested commits use imperative
  Conventional Commit summaries of at most 72 characters.
- Consider Windows/macOS separators, case, line endings, permissions, shells
  and environment conventions. Maintain equivalent behavior when applicable.
- Update entry/rules when ownership, routing, import or deployment contracts
  change; update verified workspace contracts for cross-repository changes.

## Validation and handoff

Use focused static checks from [.ai/README.md](.ai/README.md). A build requires
an explicit request and generated output must remain uncommitted. Report each
affected repository, changes, checks/results, unrun checks/reasons and deployment
caveats; never claim an unrun check passed.
