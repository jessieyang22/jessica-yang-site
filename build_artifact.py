#!/usr/bin/env python3
"""Build the Claude Artifact fragment from index.html.

index.html is the canonical page and a complete standalone document — that is what
Netlify and GitHub Pages serve. The Claude Artifact host wraps whatever it is given in
its own <!doctype html><head>...</head><body> skeleton, so publishing index.html
directly would nest a second document inside the first. This script strips index.html
back to the bare fragment the Artifact tool expects.

    python3 build_artifact.py     ->  dist/page.html

Then publish dist/page.html to the artifact, passing its existing url so it updates in
place rather than creating a second artifact.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "index.html"
OUT = ROOT / "dist" / "page.html"


def section(html: str, name: str) -> str:
    match = re.search(
        rf"<!-- artifact:{name}-start -->(.*?)<!-- artifact:{name}-end -->", html, re.S
    )
    if not match:
        sys.exit(f"index.html is missing the artifact:{name} markers")
    return match.group(1).strip()


def main() -> None:
    html = SRC.read_text()
    fragment = section(html, "head") + "\n\n" + section(html, "body") + "\n"
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(fragment)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(fragment) / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    main()
