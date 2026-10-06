# Website ownership and imports

This repository owns website infrastructure and bilingual documentation
entrances. Core/Data/BT docs stay in their owning package, application docs in
Workbench and articles/public App landing pages in `bagelquant-content`.
Never edit imported Content or `_site` manually.

The Pages workflow checks out only `bagelquant-content` from its GitHub default
branch. Package repositories, package documentation and workspace gitlink pins
are not build inputs. Do not restore package checkout, copying or doc dispatch.

Site-owned `docs/en/index.md` and `docs/cn/index.md` provide GitHub documentation
links through /content/en/docs/ and /content/cn/docs/ permalinks. They live outside
the `content/` checkout so checkout cleanup cannot remove them. Keep one entrance
per language; do not duplicate package documentation or article content.

Content's `.github/workflows/jekyll.yml` dispatches `content-updated`.
Pages collection/build/deployment remain here. A local workspace does not
change deployment's source selection.

Preserve source-revision provenance for Site and Content, including
tracked-change flags, in both Pages and local sibling-checkout modes.
Package docs remain available through their source-repository links.
Keep authored content and hosting infrastructure independently coherent and
report changes per repository.
