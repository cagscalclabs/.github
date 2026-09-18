#!/usr/bin/env python3
"""
Fetches public repos for the cagscalclabs org via the GitHub API,
sorts by stars descending, and rewrites the <!-- PROJECTS_START --> …
<!-- PROJECTS_END --> block in profile/README.md.
"""

import os
import re
import sys
from datetime import datetime, timezone
import urllib.request
import urllib.error
import json

ORG = "cagscalclabs"
MAX_REPOS = 5
README_PATH = os.path.join(os.path.dirname(__file__), "..", "profile", "README.md")

ANCHOR_START = "<!-- PROJECTS_START -->"
ANCHOR_END = "<!-- PROJECTS_END -->"

# Repos to always exclude (forks of upstream projects, meta repos, etc.)
EXCLUDE = {f"{ORG}/{ORG}", f"{ORG}/cagscalclabs_profile"}


def gh_get(path: str) -> list:
    token = os.environ.get("GITHUB_TOKEN", "")
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def fetch_repos() -> list:
    results = []
    page = 1
    while True:
        page_data = gh_get(f"/orgs/{ORG}/repos?type=public&per_page=100&page={page}")
        if not page_data:
            break
        results.extend(page_data)
        if len(page_data) < 100:
            break
        page += 1
    return results


def relative_time(iso: str) -> str:
    if not iso:
        return "unknown"
    pushed = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - pushed
    days = delta.days
    if days == 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 7:
        return f"{days} days ago"
    if days < 30:
        weeks = days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    if days < 365:
        months = days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    years = days // 365
    return f"{years} year{'s' if years > 1 else ''} ago"


def top_languages(repo: dict) -> str:
    # The list endpoint gives 'language' (primary only); good enough here.
    lang = repo.get("language")
    return lang if lang else "—"


def render_repo(repo: dict) -> str:
    name = repo["name"]
    full_name = repo["full_name"]
    url = repo["html_url"]
    description = repo.get("description") or "No description."
    stars = repo.get("stargazers_count", 0)
    lang = top_languages(repo)
    updated = relative_time(repo.get("pushed_at"))
    homepage = repo.get("homepage") or ""
    topics = repo.get("topics") or []

    # Build the extras line
    links = []
    if homepage:
        links.append(f"[Site]({homepage})")
    # Heuristic: if repo has a 'whitepaper' topic or the name suggests docs, add link
    if "whitepaper" in topics:
        links.append(
            f"[Whitepaper](https://github.com/{full_name}/releases/download/whitepaper-latest/whitepaper.pdf)"
        )
    if "docs" in topics or homepage:
        pass  # already captured via homepage

    extra = "  \n→ " + " • ".join(links) if links else ""

    stars_str = f"★ {stars}" if stars else "★ 0"

    return (
        f"**[{name}]({url})** — {description}  \n"
        f"{stars_str} &nbsp;•&nbsp; {lang} &nbsp;•&nbsp; updated {updated}"
        f"{extra}"
    )


def build_block(repos: list) -> str:
    lines = [ANCHOR_START]
    for i, repo in enumerate(repos):
        lines.append(render_repo(repo))
        if i < len(repos) - 1:
            lines.append("")
    lines.append(ANCHOR_END)
    return "\n".join(lines)


def main():
    print(f"Fetching repos for {ORG}…")
    all_repos = fetch_repos()

    # Filter: no forks, no archived, no excluded names
    filtered = [
        r for r in all_repos
        if not r.get("fork")
        and not r.get("archived")
        and r["full_name"] not in EXCLUDE
    ]

    # Sort by stars desc, break ties by recency
    filtered.sort(key=lambda r: (r.get("stargazers_count", 0), r.get("pushed_at", "")), reverse=True)
    top = filtered[:MAX_REPOS]

    print(f"Top {len(top)} repos: {[r['name'] for r in top]}")

    new_block = build_block(top)

    readme_path = os.path.realpath(README_PATH)
    with open(readme_path, "r") as f:
        content = f.read()

    pattern = re.compile(
        re.escape(ANCHOR_START) + r".*?" + re.escape(ANCHOR_END),
        re.DOTALL,
    )

    if not pattern.search(content):
        print("ERROR: anchors not found in README — nothing written.", file=sys.stderr)
        sys.exit(1)

    updated = pattern.sub(new_block, content)

    with open(readme_path, "w") as f:
        f.write(updated)

    print("README updated.")


if __name__ == "__main__":
    main()
