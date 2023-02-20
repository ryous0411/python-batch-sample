from typing import List, Dict

from src.infra.dynamodb.dynamodb_driver import IDynamoDBDriver


class GameResultDriver(IDynamoDBDriver):

    def query_by_title(self, title: str) -> List[Dict[str, str]]:
        options = {
            "TableName": self.game_table_name(),
            "IndexName": self.game_table_title_index_name(),
            "KeyConditionExpression": "title = :title",
            "ExpressionAttributeValues": {
                ":title": {'S': title}
            },
            "Limit": 10,
        }

        return self.paging_query(options)

    def put_game_result(self, game_result: Dict[str, str]) -> None:
        self.put_item(table_name=self.game_table_name(), item=game_result)
