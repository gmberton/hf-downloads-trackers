"""Refresh HF download-count badges for each tracker."""
import json
import urllib.request
from pathlib import Path

TRACKERS = {
    "tipsv2": [
        "google/tipsv2-b14",
        "google/tipsv2-l14",
        "google/tipsv2-so400m14",
        "google/tipsv2-g14",
        "google/tipsv2-b14-dpt",
        "google/tipsv2-l14-dpt",
        "google/tipsv2-so400m14-dpt",
        "google/tipsv2-g14-dpt",
    ],
}


def downloads(repo):
    url = f"https://huggingface.co/api/models/{repo}?expand[]=downloadsAllTime"
    return json.loads(urllib.request.urlopen(url).read()).get("downloadsAllTime", 0)


def fmt(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)


for name, repos in TRACKERS.items():
    total = sum(downloads(r) for r in repos)
    Path(name).mkdir(exist_ok=True)
    Path(name, "badge.json").write_text(json.dumps({
        "schemaVersion": 1,
        "label": "HF downloads",
        "message": fmt(total),
        "color": "blue",
    }, indent=2) + "\n")
    print(f"{name}: {total} -> {fmt(total)}")
