"""Push docs/store/channels/README to usabulusijock-create/bitx (no local git required)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "repos/usabulusijock-create/bitx"
GH = "gh"

RELATIVE_FILES = [
    "README.md",
    ".gitignore",
    "scripts/push_docs_github.py",
    "channels/stable.json",
    "docs/README.md",
    "docs/01-VISION.md",
    "docs/02-ARCHITECTURE.md",
    "docs/03-DIRECTORY.md",
    "docs/04-PROCESS.md",
    "docs/05-ENGINE.md",
    "docs/06-WORKBENCH.md",
    "docs/07-EXTENSION-MARKET.md",
    "docs/08-EXTENSION-HOST.md",
    "docs/09-HOST.md",
    "docs/10-SETTINGS-SECURITY.md",
    "docs/11-ROADMAP.md",
    "docs/12-CONSTRAINTS.md",
    "docs/13-UPDATES.md",
    "docs/14-EXTENDING.md",
    "store/README.md",
    "store/plugins/README.md",
    "store/mcp/README.md",
    "store/skills/README.md",
]


def gh(method: str, path: str, payload: dict | None = None) -> dict:
    cmd = [GH, "api", "--method", method, path]
    if payload is None:
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    else:
        proc = subprocess.run(
            cmd + ["--input", "-"],
            input=json.dumps(payload, ensure_ascii=False),
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr or proc.stdout)
        raise SystemExit(proc.returncode)
    return json.loads(proc.stdout) if proc.stdout.strip() else {}


def main() -> None:
    missing = [rel for rel in RELATIVE_FILES if not (ROOT / rel).is_file()]
    if missing:
        raise SystemExit("missing files: " + ", ".join(missing))

    ref = gh("GET", f"{REPO}/git/ref/heads/main")
    parent = ref["object"]["sha"]
    commit = gh("GET", f"{REPO}/git/commits/{parent}")
    base_tree = commit["tree"]["sha"]

    tree_entries = []
    for rel in RELATIVE_FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        blob = gh(
            "POST",
            f"{REPO}/git/blobs",
            {"content": text, "encoding": "utf-8"},
        )
        tree_entries.append(
            {
                "path": rel.replace("\\", "/"),
                "mode": "100644",
                "type": "blob",
                "sha": blob["sha"],
            }
        )
        print("blob", rel)

    tree = gh(
        "POST",
        f"{REPO}/git/trees",
        {"base_tree": base_tree, "tree": tree_entries},
    )
    new_commit = gh(
        "POST",
        f"{REPO}/git/commits",
        {
            "message": "docs: 同步本地设计文档与扩展货架约定\n\n公开 docs/、store/、channels/ 与 README，供开源与客户查询插件/MCP/技能。",
            "tree": tree["sha"],
            "parents": [parent],
        },
    )
    gh(
        "PATCH",
        f"{REPO}/git/refs/heads/main",
        {"sha": new_commit["sha"]},
    )
    print("pushed", new_commit["sha"])
    print("https://github.com/usabulusijock-create/bitx")


if __name__ == "__main__":
    main()
