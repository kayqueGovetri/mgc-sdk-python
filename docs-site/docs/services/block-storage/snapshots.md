---
title: Snapshots
description: Create and manage Block Storage snapshots.
---

# Snapshots

Snapshots create point-in-time copies of Block Storage volumes.

## List Snapshots

```python
snapshots = await client.block_storage.snapshots.list()

print(snapshots)
```

---

## Get Snapshot

```python
snapshot = await client.block_storage.snapshots.get(
    "YOUR_SNAPSHOT_ID"
)

print(snapshot)
```

---

## Create Snapshot

```python
snapshot = await client.block_storage.snapshots.create(
    name="before-upgrade",
    description="Snapshot before upgrading the database",
    volume_id="YOUR_VOLUME_ID",
)

print(snapshot)
```

You may identify the source volume using either:

- `volume_id`
- `volume_name`

---

## Delete Snapshot

```python
await client.block_storage.snapshots.delete(
    "YOUR_SNAPSHOT_ID"
)
```