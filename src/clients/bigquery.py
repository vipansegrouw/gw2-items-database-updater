from typing import List

from google.cloud import bigquery
from google.cloud.bigquery import TableReference, DatasetReference

from src.models.item import Item


class BigQuery():
    def client(self):
        return bigquery.client.Client(project="gw2-investment-management")

    def get_current_ids(self):
        sql = """SELECT id FROM `gw2-investment-tracker.gw2_items.gw2_items`"""
        return self.client().query(sql).result()

    def upload_items(self, items_list: List[Item]):
        json_data = []
        table_ref = TableReference(DatasetReference(self.client().project, 'gw2_items'), 'gw2_items')
        for item in items_list:
            json_data.append(item.to_dict())
        return self.client().load_table_from_json(json_rows=json_data, destination=table_ref)
