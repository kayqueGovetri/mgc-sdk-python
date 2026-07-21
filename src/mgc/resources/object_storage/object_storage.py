import boto3

from mgc.resources.object_storage.buckets import Buckets
from mgc.resources.object_storage.objects import Objects


class ObjectStorage:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
        region: str = "br-se1",
        endpoint: str | None = None,
    ):
        self._client = boto3.client(
            "s3",
            endpoint_url=f"https://{region}.magaluobjects.com",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

        self.buckets = Buckets(self._client)
        self.objects = Objects(self._client)
