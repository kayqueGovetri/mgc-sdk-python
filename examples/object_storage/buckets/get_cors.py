from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

cors = storage.buckets.get_cors("my-example-bucket")

print(cors)