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