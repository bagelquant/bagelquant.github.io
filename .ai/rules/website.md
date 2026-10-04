# Website ownership and imports

This repository is website infrastructure, not the canonical home for package,
Workbench or article content. Edit Core/Data/BT docs in their owning package,
application docs in Workbench and general articles/public App landing pages in
`bagelquant-content`. Never edit generated/copied content or `_site` manually.

Preserve the actual Pages collection boundary. The workflow checks out
`bagelquant-content` and Core/Data/BT docs from their GitHub default branches.
It does not consume workspace gitlink pins or Workbench docs. Generated docs
index pages and the copied `content/` tree belong to that build, not source
authoring. Do not introduce a second maintained content tree.

Content's `.github/workflows/jekyll.yml` only dispatches `content-updated`.
Package doc triggers dispatch `docs-updated`; Pages collection/build/deployment
remain here. A local workspace is only a development checkout and does not
change deployment's source selection.

Preserve source-revision provenance for the site plus Content/Core/Data/BT,
including tracked-change flags. Shared numerical data and Workbench are not
website build inputs. Keep authored content, generic package docs and hosting
infrastructure independently coherent and report changes per repository.
