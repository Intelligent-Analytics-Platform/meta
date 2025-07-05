from pydantic import BaseModel


class AttributeMapping(BaseModel):
    attribute: str
    description: str


class AttributeMappings(BaseModel):
    attribute_left: AttributeMapping
    attribute_right: AttributeMapping

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "attribute_left": {
                        "atrribute": "speed_water",
                        "description": "对水航速",
                    },
                    "attribute_right": {
                        "atrribute": "me_shaft_power",
                        "description": "主机功率",
                    },
                }
            ]
        }
    }
