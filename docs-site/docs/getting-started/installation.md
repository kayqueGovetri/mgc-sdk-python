---
title: Installation
description: Install and configure the MGC SDK for Python.
---

# Installation

The MGC SDK for Python is available on PyPI and supports **Python 3.11 or newer**.

## Requirements

Before installing the SDK, ensure you have:

- Python **3.11+**
- A Magalu Cloud account
- An API Token

You can verify your Python version with:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Install with pip

The recommended installation method is using `pip`.

```bash
pip install mgc-sdk-python
```

Upgrade to the latest version:

```bash
pip install --upgrade mgc-sdk-python
```

---

## Install with uv

If you use **uv** to manage dependencies:

```bash
uv add mgc-sdk-python
```

---

## Development Installation

To contribute to the project or test unreleased features:

```bash
git clone https://github.com/kayqueGovetri/mgc-sdk-python.git

cd mgc-sdk-python

pip install -e .
```

Or with development dependencies:

```bash
pip install -e ".[dev]"
```

---

## Verify the Installation

Create a Python shell:

```bash
python
```

Import the SDK:

```python
from mgc import MgcClient
```

If no errors are raised, the SDK has been installed successfully.

---

## Next Steps

After installing the SDK:

1. Generate an API Token from the Magalu Cloud Console.
2. Configure your application with the token.
3. Follow the Quick Start guide to create your first client.

```python
from mgc import MgcClient

client = MgcClient(
    api_token="YOUR_API_TOKEN"
)
```

Continue with the **Quick Start** guide to learn how to authenticate and make your first API requests.

---

## Supported Platforms

The SDK is pure Python and supports:

| Platform | Supported |
|----------|-----------|
| Linux | ✅ |
| macOS | ✅ |
| Windows | ✅ |

---

## Python Compatibility

| Python Version | Supported |
|----------------|-----------|
| 3.11 | ✅ |
| 3.12 | ✅ |
| 3.13 | ✅ |

---

## Troubleshooting

### `ModuleNotFoundError`

Ensure the package is installed in the same virtual environment used to run your application.

### Upgrade pip

If installation fails because of an outdated installer:

```bash
python -m pip install --upgrade pip
```

### Virtual Environments

Using a virtual environment is recommended for all projects:

```bash
python -m venv .venv

source .venv/bin/activate        # Linux/macOS

.venv\Scripts\activate           # Windows
```

Then install the SDK normally.

```bash
pip install mgc-sdk-python
```