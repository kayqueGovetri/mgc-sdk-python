---
title: Snapshots
description: Create and manage Virtual Machine snapshots.
---

# Snapshots

Snapshots create point-in-time copies of Virtual Machines.

## List Snapshots

```python
snapshots = await client.compute.snapshots.list(
    limit=10,
    offset=0,
    sort="created_at:desc",
)

print(snapshots)
```

---

## Get Snapshot

```python
snapshot = await client.compute.snapshots.get(
    "YOUR_SNAPSHOT_ID"
)

print(snapshot)
```

---

## Create Snapshot

```python
snapshot = await client.compute.snapshots.create(
    instance_id="YOUR_INSTANCE_ID",
    name="before-upgrade",
    description="Snapshot before upgrading the application.",
)

print(snapshot)
```

---

## Delete Snapshot

```python
await client.compute.snapshots.delete(
    "YOUR_SNAPSHOT_ID"
)
```