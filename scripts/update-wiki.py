#!/usr/bin/env python3
"""
AIX Knowledge Graph Updater
===========================
Generates graph/graph.json from wiki/ files.
Validates [[wikilinks]], updates index.md dashboard, and maintains cross-references.

Usage:
    python scripts/update-wiki.py          # Update graph.json
    python scripts/update-wiki.py --check  # Validate all wikilinks

Agent workflow: Run after editing any file in wiki/
"""

import os
import re
import json
import yaml  # pip install pyyaml
from pathlib import Path
from datetime import datetime

WIKI_DIR = Path(__file__).parent.parent / "wiki"
GRAPH_DIR = Path(__file__).parent.parent / "graph"
GRAPH_FILE = GRAPH_DIR / "graph.json"

# ── Wikilink parsing ──────────────────────────────────────────────────────

WIKILINK_RE = re.compile(r"\[\[([^\]|\\]+)(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    match = FRONTMATTER_RE.match(content)
    if match:
        try:
            return yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError:
            return {}
    return {}


def extract_wikilinks(content: str) -> list[str]:
    """Extract all [[wikilinks]] from content."""
    return WIKILINK_RE.findall(content)


def read_markdown_files() -> list[dict]:
    """Read all .md files from wiki/ and parse frontmatter + wikilinks."""
    docs = []
    for fpath in sorted(WIKI_DIR.rglob("*.md")):
        rel_path = fpath.relative_to(WIKI_DIR).with_suffix("")
        slug = str(rel_path)

        content = fpath.read_text(encoding="utf-8")
        frontmatter = extract_frontmatter(content)
        wikilinks = extract_wikilinks(content)

        # Merge frontmatter 'related' links with body wikilinks
        all_links = set(wikilinks)
        for link in frontmatter.get("related", []):
            clean_link = link.strip("[]").strip()
            all_links.add(clean_link)

        # Remove self-references
        all_links.discard(slug)

        docs.append({
            "id": slug,
            "slug": slug,
            "title": frontmatter.get("title", slug),
            "status": frontmatter.get("status", "unknown"),
            "tags": frontmatter.get("tags", []),
            "layer": frontmatter.get("layer", "unknown"),
            "updated": frontmatter.get("last_updated", "unknown"),
            "repos": frontmatter.get("repos", []),
            "links": sorted(all_links),
        })
    return docs


def build_graph(docs: list[dict]) -> dict:
    """Build knowledge graph JSON structure."""
    nodes = []
    edges = []
    doc_map = {d["slug"]: d for d in docs}

    for doc in docs:
        nodes.append({
            "id": doc["slug"],
            "title": doc["title"],
            "status": doc["status"],
            "tags": doc["tags"],
            "layer": doc["layer"],
            "updated": doc["updated"],
        })
        for link in doc["links"]:
            if link in doc_map:
                edges.append({
                    "source": doc["slug"],
                    "target": link,
                    "type": "related",
                })

    # Deduplicate edges
    unique_edges = []
    seen_edges = set()
    for edge in edges:
        key = (edge["source"], edge["target"])
        if key not in seen_edges:
            seen_edges.add(key)
            unique_edges.append(edge)

    return {
        "generated": datetime.now().isoformat(),
        "total_docs": len(nodes),
        "total_edges": len(unique_edges),
        "nodes": nodes,
        "edges": unique_edges,
    }


def validate_links(docs: list[dict]) -> list[str]:
    """Check all wikilinks resolve to existing docs."""
    slugs = {d["slug"] for d in docs}
    errors = []
    for doc in docs:
        for link in doc["links"]:
            if link not in slugs:
                errors.append(f"  [{doc['slug']}] Broken link: [[{link}]] → not found")
    return errors


def generate_index_stats(docs: list[dict], graph: dict) -> dict:
    """Generate stats for index.md dashboard."""
    by_layer = {}
    by_status = {}
    for doc in docs:
        layer = doc.get("layer", "unknown")
        status = doc.get("status", "unknown")
        by_layer[layer] = by_layer.get(layer, 0) + 1
        by_status[status] = by_status.get(status, 0) + 1

    return {
        "total_docs": len(docs),
        "total_edges": graph["total_edges"],
        "by_layer": by_layer,
        "by_status": by_status,
        "last_generated": graph["generated"],
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="AIX Knowledge Graph Updater")
    parser.add_argument("--check", action="store_true", help="Validate wikilinks only")
    args = parser.parse_args()

    docs = read_markdown_files()

    # Validate links
    errors = validate_links(docs)
    if errors:
        print(f"❌ Found {len(errors)} broken wikilinks:")
        for err in errors:
            print(err)
        if args.check:
            exit(1)
    else:
        print(f"✅ All wikilinks valid ({len(docs)} docs)")

    if args.check:
        return

    # Build graph
    graph = build_graph(docs)

    # Write graph.json
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    GRAPH_FILE.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✅ graph.json written ({len(graph['nodes'])} nodes, {graph['total_edges']} edges)")

    # Print stats
    stats = generate_index_stats(docs, graph)
    print(f"\n📊 Knowledge Graph Stats:")
    print(f"  Documents: {stats['total_docs']}")
    print(f"  Connections: {stats['total_edges']}")
    print(f"  By Layer: {json.dumps(stats['by_layer'], indent=4)}")
    print(f"  By Status: {json.dumps(stats['by_status'], indent=4)}")


if __name__ == "__main__":
    main()
