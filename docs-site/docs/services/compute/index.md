---
title: Compute
description: Provision and manage virtual machines and related compute resources.
---

# Compute

The Compute service provides everything you need to provision and manage virtual machines on Magalu Cloud.

Using the Compute API, you can:

- Create and manage virtual machines
- Browse available operating system images
- Explore available machine types
- Create and restore snapshots
- Protect workloads with backups
- Manage the virtual machine lifecycle

## Getting Started

Create a client and access the Compute service.

```python
from mgc.client import Client

async with Client(api_key="YOUR_API_TOKEN") as client:
    compute = client.compute
```

## Available Resources

| Resource | Description |
|----------|-------------|
| Virtual Machines | Create, manage and operate virtual machines. |
| Images | Browse operating system images available for deployment. |
| Machine Types | List available CPU and memory configurations. |
| Snapshots | Create point-in-time copies of virtual machines. |
| Backups | Create, restore and manage long-term backups. |

## Common Workflows

The following guides cover the most common Compute operations:

- Create your first virtual machine
- Browse available images
- Select the appropriate machine type
- Create and restore snapshots
- Protect workloads using backups
- Start, stop and reboot virtual machines

Choose one of the resources from the navigation menu to get started.