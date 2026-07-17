---
title: Quick Start
description: Create your first Magalu Cloud client and make your first API requests.
---

# Quick Start

This guide demonstrates the basic workflow for using the MGC SDK.

The typical workflow consists of:

1. Create a client
2. Authenticate
3. Access a service
4. Call an API operation

---

## Create a Client

```python
from mgc import MgcClient

client = MgcClient(
    api_token="YOUR_API_TOKEN"
)
```

---

## Access a Service

Services are exposed as attributes of the client.

Example:

```python
compute = client.compute
```

Depending on your installed SDK version, other services may include:

- Compute
- Kubernetes
- Block Storage
- Object Storage
- Networking
- Load Balancer

---

## Listing Resources

Example:

```python
instances = client.compute.instances.list()

for instance in instances:
    print(instance.name)
```

---

## Creating Resources

Example:

```python
instance = client.compute.instances.create(
    name="web-server",
    image="ubuntu-24-04",
    flavor="cloud-xs"
)
```

---

## Retrieving a Resource

```python
instance = client.compute.instances.get(
    instance_id="INSTANCE_ID"
)
```

---

## Updating a Resource

```python
client.compute.instances.update(
    instance_id="INSTANCE_ID",
    name="production-web"
)
```

---

## Deleting a Resource

```python
client.compute.instances.delete(
    instance_id="INSTANCE_ID"
)
```

---

## Error Handling

Operations may raise exceptions returned by the SDK.

```python
try:
    client.compute.instances.list()

except Exception as exc:
    print(exc)
```

Specific exception types may be available depending on the SDK version.

---

## Organizing Your Application

A common pattern is creating a single client and sharing it across your application.

```python
from mgc import MgcClient

client = MgcClient(api_token=TOKEN)

compute = client.compute
kubernetes = client.kubernetes
storage = client.object_storage
```

---

## What's Next?

Continue exploring the service documentation:

- Compute
- Kubernetes
- Block Storage
- Object Storage
- Networking
- Load Balancer

Each service includes complete examples and API reference documentation.