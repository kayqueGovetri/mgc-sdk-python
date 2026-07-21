from typing import Literal

import boto3
from botocore.exceptions import ClientError

BucketACL = Literal[
    "private",
    "public-read",
    "public-read-write",
    "authenticated-read",
]

VersioningStatus = Literal["Enabled", "Suspended"]


class Buckets:
    def __init__(self, client: boto3.client):
        self._client = client

    def list(self) -> list[dict]:
        response = self._client.list_buckets()
        return response.get("Buckets", [])

    def create(self, name: str) -> None:
        self._client.create_bucket(Bucket=name)

    def delete(self, name: str) -> None:
        self._client.delete_bucket(Bucket=name)

    def exists(self, name: str) -> bool:
        try:
            self._client.head_bucket(Bucket=name)
            return True
        except ClientError:
            return False

    def get_acl(self, name: str) -> dict:
        return self._client.get_bucket_acl(
            Bucket=name,
        )

    def set_acl(
        self,
        name: str,
        acl: BucketACL,
    ) -> None:
        self._client.put_bucket_acl(
            Bucket=name,
            ACL=acl,
        )

    def get_cors(self, name: str) -> dict:
        return self._client.get_bucket_cors(
            Bucket=name,
        )

    def set_cors(
        self,
        name: str,
        rules: list[dict],
    ) -> None:
        self._client.put_bucket_cors(
            Bucket=name,
            CORSConfiguration={
                "CORSRules": rules,
            },
        )

    def delete_cors(self, name: str) -> None:
        self._client.delete_bucket_cors(
            Bucket=name,
        )

    def get_policy(self, name: str) -> dict:
        return self._client.get_bucket_policy(
            Bucket=name,
        )

    def set_policy(
        self,
        name: str,
        policy: str,
    ) -> None:
        self._client.put_bucket_policy(
            Bucket=name,
            Policy=policy,
        )

    def delete_policy(self, name: str) -> None:
        self._client.delete_bucket_policy(
            Bucket=name,
        )

    def get_versioning(self, name: str) -> dict:
        return self._client.get_bucket_versioning(
            Bucket=name,
        )

    def set_versioning(
        self,
        name: str,
        status: VersioningStatus,
    ) -> None:
        self._client.put_bucket_versioning(
            Bucket=name,
            VersioningConfiguration={
                "Status": status,
            },
        )

    def public_url(self, name: str) -> str: ...
