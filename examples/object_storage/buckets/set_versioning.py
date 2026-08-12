from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

storage.buckets.set_versioning(
    "my-example-bucket",
    "Enabled",
)
