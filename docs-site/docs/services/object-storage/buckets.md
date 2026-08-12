---
title: Buckets
description: Manage buckets and bucket configuration in Object Storage.
---

# Buckets

Buckets are containers used to organize and store objects in Object Storage.

They provide the foundation for storing files and other data, while allowing you to configure access control, CORS, bucket policies and versioning.

## Getting Started

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)
```

## Available Operations

| Operation      | Description                                   |
| -------------- | --------------------------------------------- |
| Create         | Create a new bucket.                          |
| Delete         | Delete an existing bucket.                    |
| Exists         | Check whether a bucket exists.                |
| List           | List available buckets.                       |
| Get ACL        | Retrieve the bucket access control list.      |
| Set ACL        | Configure the bucket access control list.     |
| Get CORS       | Retrieve the bucket CORS configuration.       |
| Set CORS       | Configure the bucket CORS rules.              |
| Delete CORS    | Remove the bucket CORS configuration.         |
| Get Policy     | Retrieve the bucket policy.                   |
| Set Policy     | Configure the bucket policy.                  |
| Delete Policy  | Remove the bucket policy.                     |
| Get Versioning | Retrieve the bucket versioning configuration. |
| Set Versioning | Configure bucket versioning.                  |

## Create a Bucket

Create a new bucket by providing its name.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.create("my-bucket")
```

## Delete a Bucket

Delete an existing bucket by providing its name.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.delete("my-example-bucket")
```

## Check if a Bucket Exists

Use `exists` to check whether a bucket exists.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

exists = storage.buckets.exists("my-example-bucket")

print(exists)
```

## List Buckets

Use `list` to retrieve the available buckets.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

buckets = storage.buckets.list()

for bucket in buckets:
    print(bucket)
```

## Access Control List (ACL)

Bucket ACLs control access permissions for a bucket.

### Get ACL

Retrieve the current ACL configuration of a bucket.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

acl = storage.buckets.get_acl("my-example-bucket")

print(acl)
```

### Set ACL

Configure the ACL of a bucket.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.set_acl(
    "my-example-bucket",
    "private",
)
```

## CORS

Cross-Origin Resource Sharing (CORS) allows applications running in different origins to access objects stored in a bucket.

### Get CORS

Retrieve the current CORS configuration.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

cors = storage.buckets.get_cors("my-example-bucket")

print(cors)
```

### Set CORS

Configure the CORS rules for a bucket.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.set_cors(
    "my-example-bucket",
    [
        {
            "AllowedMethods": ["GET", "PUT"],
            "AllowedOrigins": ["*"],
            "AllowedHeaders": ["*"],
            "ExposeHeaders": ["ETag"],
            "MaxAgeSeconds": 3000,
        }
    ],
)
```

### Delete CORS

Remove the CORS configuration from a bucket.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.delete_cors("my-example-bucket")
```

## Bucket Policy

Bucket policies define permissions for accessing resources stored in a bucket.

### Get Policy

Retrieve the current bucket policy.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

policy = storage.buckets.get_policy("my-example-bucket")

print(policy)
```

### Set Policy

Set a bucket policy using a JSON policy document.

```python
import json

from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*",
        }
    ],
}

storage.buckets.set_policy(
    name="my-bucket",
    policy=json.dumps(policy),
)
```

### Delete Policy

Remove the bucket policy.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.delete_policy("my-example-bucket")
```

## Versioning

Bucket versioning allows multiple versions of an object to be maintained.

### Get Versioning

Retrieve the current versioning configuration.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

versioning = storage.buckets.get_versioning("my-example-bucket")

print(versioning)
```

### Set Versioning

Configure the versioning state of a bucket.

```python
from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.set_versioning(
    "my-example-bucket",
    "Enabled",
)
```
