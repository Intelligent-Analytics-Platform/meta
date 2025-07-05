from pydantic import BaseModel


class TimeZone(BaseModel):
    code: str
    name_cn: str
    name_en: str
    explaination: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "UTC+8",
                    "name_cn": "中国标准时间",
                    "name_en": "China Standard Time",
                }
            ]
        }
    }
