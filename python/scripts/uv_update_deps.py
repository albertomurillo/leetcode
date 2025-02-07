#!/usr/bin/env python3

import subprocess
import tomllib
from pathlib import Path

with Path("pyproject.toml").open("rb") as fp:
    config = tomllib.load(fp)

# Dependencies
deps = config.get("project", {}).get("dependencies", [])
deps = [dep.split(">=")[0] for dep in deps if ">=" in dep]
if deps:
    subprocess.run(["uv", "remove", *deps], check=False)  # noqa: S603, S607
    subprocess.run(["uv", "add", *deps], check=False)  # noqa: S603, S607

# Dev Dependencies
deps = config.get("dependency-groups", {}).get("dev", {})
deps = [dep.split(">=")[0] for dep in deps if ">=" in dep]
if deps:
    subprocess.run(["uv", "remove", "--dev", *deps], check=False)  # noqa: S603, S607
    subprocess.run(["uv", "add", "--dev", *deps], check=False)  # noqa: S603, S607
