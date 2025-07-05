from pydantic import BaseModel


class LabelValue(BaseModel):
    label: str
    value: str

    model_config = {
        "json_schema_extra": {"examples": [{"label": "液化天然气", "value": "lng"}]}
    }
