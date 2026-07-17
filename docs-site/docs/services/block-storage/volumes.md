---
title: Volumes
description: Create and manage Block Storage volumes.
---

# Volumes

Volumes provide persistent storage that can be attached to Virtual Machines.

## List Volumes

```python
volumes = await client.block_storage.volumes.list(
    limit=10,
    offset=0,
)

print(volumes)
```

---

## Get Volume

```python
volume = await client.block_storage.volumes.get(
    "YOUR_VOLUME_ID"
)

print(volume)
```

---

## Create Volume

```python
volume = await client.block_storage.volumes.create(
    name="database-volume",
    size=100,
    type_id="YOUR_VOLUME_TYPE_ID",
)

print(volume)
```

You may also create a volume from:

- a backup (`backup_id` or `backup_name`)
- a snapshot (`snapshot_id` or `snapshot_name`)

---

## Rename Volume

```python
await client.block_storage.volumes.rename(
    "YOUR_VOLUME_ID",
    name="database-volume-prod",
)
```

---

## Extend a Volume

```python
await client.block_storage.volumes.extend(
    "YOUR_VOLUME_ID",
    size=200,
)
```

---

## Change Volume Type

```python
await client.block_storage.volumes.retype(
    "YOUR_VOLUME_ID",
    type_id="YOUR_NEW_VOLUME_TYPE_ID",
)
```

---

## Attach a Volume

```python
await client.block_storage.volumes.attach(
    "YOUR_VOLUME_ID",
    instance_id="YOUR_INSTANCE_ID",
)
```

---

## Detach a Volume

```python
await client.block_storage.volumes.detach(
    "YOUR_VOLUME_ID",
)
```

---

## List Available Volume Types

```python
volume_types = await client.block_storage.volumes.get_volume_types()

print(volume_types)
```

---

## Delete Volume

```python
await client.block_storage.volumes.delete(
    "YOUR_VOLUME_ID"
)
```