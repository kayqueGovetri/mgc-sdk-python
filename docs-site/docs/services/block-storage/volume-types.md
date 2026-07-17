---
title: Volume Types
description: Browse available Block Storage volume types.
---

# Volume Types

Volume Types define the performance characteristics available for Block Storage volumes.

Use this operation to discover the available storage classes before creating or changing a volume.

## List Volume Types

```python
volume_types = await client.block_storage.volumes.get_volume_types()

print(volume_types)
```

The returned information can be used when:

- Creating a new volume (`type_id`)
- Changing the type of an existing volume (`retype()`)