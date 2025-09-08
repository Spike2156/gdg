# VK Reposter

This repository contains a simple script that monitors a source VK community and
reposts new entries to a target group.

## Requirements

- Python 3
- [`vk_api`](https://pypi.org/project/vk-api/) library

Install dependencies:

```bash
pip install vk_api
```

## Usage

Set environment variables with your credentials and group IDs:

```bash
export SOURCE_GROUP_ID=123456       # numeric ID of the source community
export TARGET_GROUP_ID=654321       # numeric ID of your group
export SOURCE_TOKEN=...             # token with permissions to read source posts
export TARGET_TOKEN=...             # token with permissions to post to your group
```

(Optional) configure polling:

```bash
export FETCH_COUNT=5       # number of recent posts to check each cycle
export POLL_INTERVAL=10    # delay between checks in seconds
```

Run the script:

```bash
python vk_reposter.py
```

The script will continuously check the source community and publish new posts to
your group.
