import abc
from typing import Any

import boto3
from botocore.client import BaseClient

dynamodb: BaseClient = boto3.client("dynamodb", endpoint_url="http://localhost:8000")


class IDynamoDBDriver(metaclass=abc.ABCMeta):

    @staticmethod
    def game_table_name() -> str:
        return "game"

    @staticmethod
    def game_table_title_index_name() -> str:
        return "title-index"

    @staticmethod
    def paging_query(options) -> list[dict]:

        total_results = []
        while True:
            results = dynamodb.query(**options)
            total_results += results.get("Items", [])
            if "LastEvaluatedKey" not in results:
                break
            options["ExclusiveStartKey"] = results["LastEvaluatedKey"]

        return total_results

    @staticmethod
    def put_item(table_name: str, item: dict) -> Any:
        return dynamodb.put_item(TableName=table_name, Item=item)
