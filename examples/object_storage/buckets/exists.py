from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

exists = storage.buckets.exists("my-example-bucket")

print(exists)