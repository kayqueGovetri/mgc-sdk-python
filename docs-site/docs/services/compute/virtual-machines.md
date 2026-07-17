---
title: Virtual Machines
description: Manage virtual machines with the MGC Python SDK.
---

# Virtual Machines

The Virtual Machines API allows you to create and manage compute instances on Magalu Cloud.

All operations are asynchronous.

```python
from mgc.client import Client

async with Client(api_key="YOUR_API_TOKEN") as client:
    ...
```

---

# Listing Virtual Machines

Retrieve a paginated list of virtual machines.

```python
virtual_machines = await client.compute.virtual_machines.list(
    limit=10,
    offset=0,
    sort="created_at:desc",
)

print(virtual_machines)
```

---

# Getting a Virtual Machine

Retrieve detailed information about a virtual machine.

```python
virtual_machine = await client.compute.virtual_machines.get(
    "YOUR_INSTANCE_ID",
    expand=["image", "machine_type"],
)

print(virtual_machine)
```

---

# Creating a Virtual Machine

Provision a new virtual machine.

```python
virtual_machine = await client.compute.virtual_machines.create(
    name="example-instance",
    image_id="YOUR_IMAGE_ID",
    machine_type_id="YOUR_MACHINE_TYPE_ID",
    ssh_key_name="YOUR_SSH_KEY_NAME",
)
```

---

# Renaming a Virtual Machine

```python
await client.compute.virtual_machines.rename(
    "YOUR_INSTANCE_ID",
    name="example-instance-renamed",
)
```

---

# Changing the Machine Type

```python
await client.compute.virtual_machines.retype(
    "YOUR_INSTANCE_ID",
    machine_type_id="YOUR_MACHINE_TYPE_ID",
)
```

---

# Starting a Virtual Machine

```python
await client.compute.virtual_machines.start(
    "YOUR_INSTANCE_ID"
)
```

---

# Stopping a Virtual Machine

```python
await client.compute.virtual_machines.stop(
    "YOUR_INSTANCE_ID"
)
```

---

# Rebooting a Virtual Machine

```python
await client.compute.virtual_machines.reboot(
    "YOUR_INSTANCE_ID"
)
```

---

# Suspending a Virtual Machine

```python
await client.compute.virtual_machines.suspend(
    "YOUR_INSTANCE_ID"
)
```

---

# Deleting a Virtual Machine

```python
await client.compute.virtual_machines.delete(
    "YOUR_INSTANCE_ID",
    delete_public_ip=False,
)
```