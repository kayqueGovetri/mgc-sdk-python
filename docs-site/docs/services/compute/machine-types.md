---
title: Machine Types
description: Browse available machine types.
---

# Machine Types

Machine Types define the CPU, memory and hardware configuration of a Virtual Machine.

## List Machine Types

Retrieve all available machine types.

```python
machine_types = await client.compute.machine_types.list(
    limit=10,
    offset=0,
    sort="name:asc",
)

print(machine_types)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| limit | Maximum number of machine types returned. |
| offset | Number of records to skip. |
| sort | Sorting expression. |
| expand | Expand related resources. |

## Next Steps

Use the returned `id` when creating or changing a Virtual Machine.

```python
await client.compute.virtual_machines.create(
    machine_type_id="YOUR_MACHINE_TYPE_ID",
    ...
)
```