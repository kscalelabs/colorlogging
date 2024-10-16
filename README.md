<p align="center">
  <picture>
    <img alt="K-Scale Open Source Robotics" src="https://media.kscale.dev/kscale-open-source-header.png" style="max-width: 100%;">
  </picture>
</p>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kscalelabs/urdf2mjcf/blob/main/LICENSE)
[![Version](https://img.shields.io/pypi/v/urdf2mjcf)](https://pypi.org/project/urdf2mjcf/)
[![Discord](https://img.shields.io/discord/1224056091017478166)](https://discord.gg/kscale)
[![Wiki](https://img.shields.io/badge/wiki-humanoids-black)](https://humanoids.wiki)
<br />
[![python](https://img.shields.io/badge/-Python_3.11-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![ruff](https://img.shields.io/badge/Linter-Ruff-red.svg?labelColor=gray)](https://github.com/charliermarsh/ruff)

</div>

# colorlogging

Makes logging colorful!

<p align="center">
  <img src="./docs/example.png" alt="Example of colorlogging output">
</p>

<p align="center">
  <em>Example of colorlogging output</em>
</p>

## Installation

Simply run

```bash
pip install colorlogging
```

## Usage

To configure logging, call `configure_logging` like so:

```python
import colorlogging
import logging

logger = logging.getLogger(__name__)

def main() -> None:
    colorlogging.configure()
    logger.info("Hello, world!")
```

This tool also provides some other helpful display functions:

```python
import colorlogging

colorlogging.show_info("This is a status message", important=True)
colorlogging.show_warning("This is a warning message")
colorlogging.show_error("This is an error message")
```

This shows the following output:

<p align="center">
  <img src="./docs/example2.png" alt="Another example of colorlogging output">
</p>
