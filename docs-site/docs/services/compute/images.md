---
title: Images
description: Browse available operating system images.
---

# Images

Images are bootable operating system templates used when provisioning virtual machines.

The Compute service provides a catalog of available images that can be used when creating new instances.

## List Images

Retrieve the list of available images.

```python
images = await client.compute.images.list(
    limit=10,
    offset=0,
    sort="name:asc",
)

print(images)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| limit | Maximum number of images returned. |
| offset | Number of records to skip. |
| sort | Sorting expression. |
| expand | Expand related resources. |

## Next Steps

After selecting an image, use its `id` when creating a Virtual Machine.

```python
await client.compute.virtual_machines.create(
    image_id="YOUR_IMAGE_ID",
    ...
)
```