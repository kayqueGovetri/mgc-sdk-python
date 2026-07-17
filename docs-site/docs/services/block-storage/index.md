---
title: Block Storage
description: Manage persistent block storage resources.
---

# Block Storage

Block Storage provides persistent volumes that can be attached to virtual machines.

Volumes remain available independently of the lifecycle of a virtual machine, making them suitable for databases, applications and persistent workloads.

## Getting Started

```python
from mgc.client import Client

async with Client(api_key="YOUR_API_TOKEN") as client:
    block_storage = client.block_storage
```

## Available Resources

| Resource | Description |
|----------|-------------|
| Volumes | Create and manage persistent storage volumes. |
| Snapshots | Create point-in-time copies of volumes. |
| Volume Types | Browse available storage classes. |