---
title: Authentication
description: Learn how to authenticate with the MGC SDK for Python.
---

# Authentication

The MGC SDK authenticates using a **Magalu Cloud API Token**.

Before using the SDK, generate an API Token from your Magalu Cloud account.

---

## Generate an API Token

1. Sign in to the Magalu Cloud Console.
2. Navigate to **API Tokens**.
3. Create a new token.
4. Copy and store the token securely.

> Keep your API Token secret. Never commit it to source control or expose it publicly.

---

## Creating a Client

Pass your API Token when creating the client.

```python
from mgc import MgcClient

client = MgcClient(
    api_token="YOUR_API_TOKEN"
)
```

Once the client has been created, it can be reused throughout your application.

---

## Using Environment Variables

The recommended approach is storing your token in an environment variable.

### Linux/macOS

```bash
export MGC_API_TOKEN="YOUR_API_TOKEN"
```

### Windows PowerShell

```powershell
$env:MGC_API_TOKEN="YOUR_API_TOKEN"
```

Then:

```python
import os

from mgc import MgcClient

client = MgcClient(
    api_token=os.environ["MGC_API_TOKEN"]
)
```

---

## Using a `.env` File

You may also use `python-dotenv`.

Install:

```bash
pip install python-dotenv
```

Create a `.env` file:

```text
MGC_API_TOKEN=YOUR_API_TOKEN
```

Load it:

```python
import os

from dotenv import load_dotenv

from mgc import MgcClient

load_dotenv()

client = MgcClient(
    api_token=os.environ["MGC_API_TOKEN"]
)
```

---

## Security Best Practices

- Never commit API tokens.
- Never hardcode secrets in your source code.
- Rotate tokens periodically.
- Use separate tokens for development and production.
- Grant only the permissions required for your application.

---

## Reusing the Client

Creating a client is lightweight, but applications typically instantiate it once and reuse it.

```python
client = MgcClient(api_token=TOKEN)

compute = client.compute
network = client.network
storage = client.object_storage
```

---

## Next Steps

Now that authentication is configured, continue with the **Quick Start** guide to perform your first API requests.