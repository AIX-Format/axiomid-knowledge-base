# AIX Sovereign Stack — Knowledge Base

> Codename: Echo369 | Spec: AIX/1.0 | v0.369.0

This is the central knowledge base for the AIX Sovereign Stack — a 7-repo ecosystem that powers decentralized human-AI collaboration on Pi Network.

## Structure

```
AIX-Knowledge-Base/
├── wiki/              ← Main content (markdown with YAML frontmatter + [[wikilinks]])
│   ├── index.md       ← Dashboard
│   ├── *.md           ← Documents for each layer and topic
│   └── sessions/      ← Session logs
├── graph/
│   └── graph.json     ← Auto-generated knowledge graph
├── schemas/
│   └── template.md    ← Reusable template
├── scripts/
│   ├── update-wiki.py ← Regenerate graph.json
│   └── validate-links.py ← Check all wikilinks
├── legacy/            ← Original .md files backup
├── repos/             ← Symlinks to the 7 repos
├── core-files/        ← Core AIX files
├── agents-instructions.md  ← Agent workflow rules
└── README.md          ← This file
```

## Quick Start

### For Humans
- Open `wiki/index.md` for the dashboard
- Use `[[wikilinks]]` to navigate between documents
- Open the folder in **Obsidian** for graph view + search (free)

### For Agents
- Read `agents-instructions.md` for workflow rules
- Frontmatter contains machine-parseable metadata
- `scripts/update-wiki.py` validates and regenerates the graph

## The Stack

| Layer | Repo | Role |
|-------|------|------|
| L0 | axiomid-project | Identity & XP |
| L1 | aix-format | Protocol & DNA |
| L2 | iqra | Runtime & Memory |
| L3 | aix-agent-skills | Marketplace |
| L4 | AlphaAxiom | Trading |
| L5 | PiWorker-OS | Pi Treasury |
| L6 | GemClaw | Voice |

**Real code**: ~136,544 lines | **Files**: 1,196 | **TypeScript**: 63%

## Deployment

This knowledge base is deployed as a static site via **Quartz** on GitHub Pages:
[https://aix-format.github.io/axiomid-knowledge-base](https://aix-format.github.io/axiomid-knowledge-base)

## License

See the AIX Sovereign Stack license.
