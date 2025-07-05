from pydantic import BaseModel


class ShipType(BaseModel):
    code: str
    name_cn: str
    name_en: str
    cii_related_tone: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "I1004",
                    "name_cn": "集装箱船",
                    "name_en": "Container Ship",
                    "cii_related_tone": "DWT",
                }
            ]
        }
    }
