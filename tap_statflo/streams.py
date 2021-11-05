"""Stream type classes for tap-statflo."""

from pathlib import Path
from datetime import datetime
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_statflo.client import statfloStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class CustomerActivityStream(statfloStream):
    """Define custom stream."""
    name = "customer-activity"
    path = "/customer-activity"
    primary_keys = []
    replication_key = None
    records_jsonpath = "$.customer-activity[*]"
    
    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        start_date = self._config.get("start_date")
        start_date = start_date.split("T")[0]
        end_date = datetime.now().strftime("%Y-%m-%d")
        dealer_id = self._config.get("dealer_id")
        
        return {"statflo_dealer_id": dealer_id, "start_date": start_date, "end_date": end_date}
    
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("action_taken", th.StringType),
        th.Property("ban_id", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("date_added", th.DateTimeType),
        th.Property("dealer_id", th.IntegerType),
        th.Property("dealer_name", th.StringType),
        th.Property("lead_code", th.StringType),
        th.Property("message", th.StringType),
        th.Property("message_from", th.StringType),
        th.Property("message_template_id", th.StringType),
        th.Property("message_to", th.StringType),
        th.Property("next_date", th.DateTimeType),
        th.Property("next_steps", th.StringType),
        th.Property("outcome_reason", th.StringType),
        th.Property("outlet_id", th.StringType),
        th.Property("record_source", th.StringType),
        th.Property("subject", th.StringType),
        th.Property("type", th.IntegerType),
        th.Property("type_description", th.StringType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("user_email", th.StringType),
        th.Property("user_id", th.IntegerType)
    ).to_dict()
