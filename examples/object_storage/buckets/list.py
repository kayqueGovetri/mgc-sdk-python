from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

buckets = storage.buckets.list()

for bucket in buckets:
    print(bucket)
