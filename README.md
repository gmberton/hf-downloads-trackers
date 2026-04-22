# hf-downloads-trackers

Daily-updated download-count badges for Hugging Face model collections. A GitHub Action sums `downloadsAllTime` across a tracker's repo list once a day and writes `<tracker>/badge.json`, served via GitHub Pages. The badge is rendered by [shields.io](https://shields.io)'s `endpoint` feature.

## Trackers

### tipsv2

[![HF downloads](https://img.shields.io/endpoint?url=https://gmberton.github.io/hf-downloads-trackers/tipsv2/badge.json)](https://huggingface.co/collections/google/tipsv2)

All 8 variants of [Google TIPSv2](https://huggingface.co/collections/google/tipsv2): `tipsv2-{b14,l14,so400m14,g14}` ± `-dpt`.

## Add a tracker

Append an entry to `TRACKERS` in `update.py` with a name and a list of HF repo IDs. The next daily run creates `<name>/badge.json`; embed it with:

```
https://img.shields.io/endpoint?url=https://gmberton.github.io/hf-downloads-trackers/<name>/badge.json
```
