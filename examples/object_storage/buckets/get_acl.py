from mgc.resources.object_storage.object_storage import ObjectStorage

storage = ObjectStorage(
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)

acl = storage.buckets.get_acl("my-example-bucket")

print(acl)