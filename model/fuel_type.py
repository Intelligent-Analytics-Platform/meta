from pydantic import BaseModel


class FuelType(BaseModel):
    code: str
    name_cn: str
    name_en: str
    cf: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "LNG",
                    "name_cn": "液化天然气 (LNG)",
                    "name_en": "Liquefied Natural Gas (LNG)",
                    "cf": 2.75,
                }
            ]
        }
    }
