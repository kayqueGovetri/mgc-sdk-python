# MGC SDK for Python

[![PyPI](https://img.shields.io/pypi/v/mgc-sdk-python)](https://pypi.org/)
[![Python](https://img.shields.io/pypi/pyversions/mgc-sdk-python)](https://pypi.org/)

An unofficial, open-source Python SDK for interacting with the Magalu Cloud API.

This project aims to provide a Pythonic and developer-friendly interface for Magalu Cloud services, inspired by the official Go SDK while remaining completely independent from Magalu Cloud and its maintainers. The project is community-driven and maintained by contributors.

> **Disclaimer**
>
> This is an unofficial SDK and is not affiliated with, endorsed by, or maintained by Magalu Cloud. For the official SDKs and tools, visit the Magalu Cloud GitHub organization.

## Features

- Pythonic API design
- Async support using `httpx`
- Typed models with Pydantic
- Modular service architecture
- Easy authentication using API Tokens
- Open-source and community-driven
- Designed for automation, scripting, and backend applications

## Installation

### Using pip

```bash
pip install mgc-sdk
```

### Development installation

```bash
git clone https://github.com/kayqueGovetri/mgc-sdk-python.git

cd mgc-sdk-python

pip install -e .
```

## Quick Start

```python
from mgc import MgcClient

client = MgcClient(
    api_token="YOUR_API_TOKEN"
)

instances = client.compute.instances.list()

for instance in instances:
    print(instance.name)
```

## Authentication

The SDK authenticates using a Magalu Cloud API Token.

```python
from mgc import MgcClient

client = MgcClient(
    api_token="YOUR_API_TOKEN"
)
```

For information about generating API tokens, consult the official Magalu Cloud documentation. :contentReference[oaicite:1]{index=1}

## Supported Services

Current implementation status:

### Compute

- [x] Instances
- [x] Images
- [x] Machine Types
- [x] Snapshots

### Block Storage

- [ ] Volumes
- [ ] Snapshots
- [ ] Volume Types

### Networking

- [ ] VPCs
- [ ] Subnets
- [ ] Security Groups
- [ ] Public IPs

### Kubernetes

- [ ] Clusters
- [ ] Node Pools

### Database

- [ ] DBaaS Instances
- [ ] Replicas
- [ ] Snapshots

> The roadmap evolves based on community contributions and API availability.

## Async Example

```python
import asyncio

from mgc import AsyncMgcClient


async def main():
    client = AsyncMgcClient(
        api_token="YOUR_API_TOKEN"
    )

    instances = await client.compute.instances.list()

    print(instances)


asyncio.run(main())
```

## Project Structure

```text
mgc-sdk-python/
├── mgc/
│   ├── client/
│   ├── compute/
│   ├── networking/
│   ├── models/
│   ├── exceptions/
│   └── utils/
├── tests/
├── examples/
└── docs/
```

## Why This Project?

While Magalu Cloud provides official tooling and SDKs, Python developers may prefer a native Python experience for:

- Automation
- Infrastructure management
- Data engineering
- Backend services
- Serverless applications
- Scripts and CLI tools

This project seeks to fill that gap with a modern Python SDK.

## Contributing

Contributions are welcome.

You can contribute by:

- Reporting bugs
- Suggesting new features
- Improving documentation
- Adding support for new services
- Writing tests

### Running tests

```bash
pytest
```

### Linting

```bash
ruff check .
```

### Formatting

```bash
ruff format .
```

## Roadmap

- [ ] Full Compute API coverage
- [ ] Networking support
- [ ] Kubernetes support
- [ ] DBaaS support
- [ ] Object Storage support
- [ ] CLI integration
- [ ] Complete documentation
- [ ] Automated releases

## Related Projects

- Official Magalu Cloud Go SDK
- Official Magalu Cloud Organization

See the [LICENSE](LICENSE) file for details.

---

Built and maintained by the open-source community.
