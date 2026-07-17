---
title: Backups
description: Create and manage Virtual Machine backups.
---

# Backups

Backups provide long-term protection for Virtual Machines.

## List Backups

```python
backups = await client.compute.backups.list(
    expand=["instance"],
)

print(backups)
```

---

## Get Backup

```python
backup = await client.compute.backups.get(
    "YOUR_BACKUP_ID",
    expand=["instance"],
)

print(backup)
```

---

## Create Backup

```python
backup = await client.compute.backups.create(
    instance_id="YOUR_INSTANCE_ID",
    name="daily-backup",
)

print(backup)
```

---

## Rename Backup

```python
await client.compute.backups.rename(
    "YOUR_BACKUP_ID",
    name="production-backup"
)
```

---

## Copy Backup

```python
await client.compute.backups.copy(
    "YOUR_BACKUP_ID",
    region="br-ne1",
)
```

---

## Delete Backup

```python
await client.compute.backups.delete(
    "YOUR_BACKUP_ID"
)
```