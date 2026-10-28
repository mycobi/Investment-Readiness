"""Dependency-free checks for repository Markdown and internal file links."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

def check(root):
    errors = []
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8-sig")
        name = path.relative_to(root)
        fence = None
        table_width = None
        for number, line in enumerate(text.splitlines(), 1):
            prefix = f"{name}:{number}"
            if "\u2014" in line:
                errors.append(f"{prefix}: em dash is not allowed")
            if "\t" in line:
                errors.append(f"{prefix}: use spaces instead of tabs")
            marker = re.match(r"^\s*(" + chr(96) + r"{3,}|~{3,})", line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                continue
            if fence:
                continue
            if line.startswith("|") and line.rstrip().endswith("|"):
                width = len(re.split(r"(?<!\\)\|", line.strip())) - 2
                if table_width is not None and width != table_width:
                    errors.append(f"{prefix}: inconsistent table column count")
                table_width = width
            else:
                table_width = None
            for match in re.finditer(r"\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+\"[^\"]*\")?\)", line):
                link = match.group(1).strip("<>")
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                    continue
                target = unquote(link.split("#", 1)[0].split("?", 1)[0])
                if target and not (path.parent / target).exists():
                    errors.append(f"{prefix}: missing internal target {target}")
        if fence:
            errors.append(f"{name}: unclosed code fence")
    return errors

if __name__ == "__main__":
    errors = check(Path(__file__).resolve().parents[1])
    for error in errors:
        print(error)
    if errors:
        sys.exit(1)
    print("Documentation checks passed: Markdown structure and internal file links.")
    print("External URLs, heading anchors, legal validity and confidentiality require separate review.")
