from model.attribute_mapping import AttributeMapping, AttributeMappings
from model.fuel_type import FuelType
from model.label_value import LabelValue
from model.ship_type import ShipType
from model.time_zone import TimeZone


def get_meta_service():
    """获取 MetaService 实例"""
    return MetaService()


class MetaService:
    def get_all_fuel_types(self) -> list[FuelType]:
        """获取所有燃料类型"""
        return [
            FuelType(
                code="HFO-HS",
                name_cn="重燃油 (HFO) 硫含量高于0.5% m/m",
                name_en="HFO, S>0.5% m/m",
                cf=3.114,
            ),
            FuelType(
                code="HFO-LS",
                name_cn="重燃油 (HFO) 硫含量不高于0.1% m/m, 但不高于0.5% m/m",
                name_en="HFO, 0.1% m/m<=S<=0.5% m/m",
                cf=3.114,
            ),
            FuelType(
                code="HFO-ULS",
                name_cn="重燃油 (HFO) 硫含量不高于0.1% m/m",
                name_en="HFO, S<=0.1% m/m",
                cf=3.114,
            ),
            FuelType(
                code="LFO-HS",
                name_cn="轻燃油 (LFO) 硫含量高于0.5% m/m",
                name_en="LFO, S>0.5% m/m",
                cf=3.151,
            ),
            FuelType(
                code="LFO-LS",
                name_cn="轻燃油 (LFO) 硫含量不高于0.1% m/m, 但不高于0.5% m/m",
                name_en="LFO, 0.1% m/m<=S<=0.5% m/m",
                cf=3.151,
            ),
            FuelType(
                code="LFO-ULS",
                name_cn="轻燃油 (LFO) 硫含量不高于0.1% m/m",
                name_en="LFO, S<=0.1% m/m",
                cf=3.151,
            ),
            FuelType(
                code="MDO/MGO",
                name_cn="船用柴油",
                name_en="MDO/MGO",
                cf=3.206,
            ),
            FuelType(
                code="MDO/MGO-RIVER",
                name_cn="内河船用燃料油",
                name_en="MDO/MGO for River Boat",
                cf=3.206,
            ),
            FuelType(
                code="LPG-Propane",
                name_cn="液化石油气 (LPG) 丙烷",
                name_en="LPG-Propane",
                cf=3.0,
            ),
            FuelType(
                code="LPG-Butane",
                name_cn="液化石油气 (LPG) 丁烷",
                name_en="LPG-Butane",
                cf=3.03,
            ),
            FuelType(
                code="LNG",
                name_cn="液化天然气 (LNG)",
                name_en="Liquefied Natural Gas (LNG)",
                cf=2.75,
            ),
            FuelType(
                code="Methanol",
                name_cn="甲醇",
                name_en="Methanol",
                cf=1.375,
            ),
            FuelType(code="Ethanol", name_cn="乙醇", name_en="Ethanol", cf=1.913),
            FuelType(code="Ethane", name_cn="乙烷", name_en="Ethane", cf=2.927),
            FuelType(code="Ammonia", name_cn="氨", name_en="Ammonia", cf=0.0),
            FuelType(code="Hydrogen", name_cn="氢", name_en="Hydrogen", cf=0.0),
        ]

    def get_all_ship_types(self) -> list[ShipType]:
        """获取所有船舶类型"""
        return [
            ShipType(
                cii_related_tone="dwt",
                name_cn="散货船",
                name_en="Bulk carrier",
                code="I001",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="散货船",
                name_en="Bulk carrier",
                code="I001",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="气体运输船",
                name_en="Gas carrier",
                code="I002",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="液货船",
                name_en="Tanker",
                code="I003",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="集装箱船",
                name_en="Container ship",
                code="I004",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="杂货船",
                name_en="General cargo ship",
                code="I005",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="冷藏货船",
                name_en="Refrigerated cargo carrier",
                code="I006",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="兼用船",
                name_en="Combination carrier",
                code="I007",
            ),
            ShipType(
                cii_related_tone="dwt",
                name_cn="LNG运输船",
                name_en="LNG carrier",
                code="I008",
            ),
            ShipType(
                cii_related_tone="gt",
                name_cn="滚装货船（车辆运输船）",
                name_en="Ro-ro cargo ship (vehicle carrier)",
                code="I009",
            ),
            ShipType(
                cii_related_tone="gt",
                name_cn="滚装货船",
                name_en="Ro-ro cargo ship",
                code="I010",
            ),
            ShipType(
                cii_related_tone="gt",
                name_cn="客滚船",
                name_en="Ro-ro passenger ship",
                code="I011",
            ),
            ShipType(
                cii_related_tone="gt",
                name_cn="客滚船(高速)",
                name_en="Ro-ro passenger ship (high-speed craft)",
                code="I011.1",
            ),
            ShipType(
                cii_related_tone="gt",
                name_cn="豪华邮轮",
                name_en="Cruise passenger ship",
                code="I012",
            ),
        ]

    def get_all_time_zones(self) -> list[TimeZone]:
        """获取所有时区"""
        return [
            TimeZone(
                code="UTC+0",
                name_cn="零时区",
                name_en="UTC+0",
                explaination="零时区 7.5° W～7.5° E 0°",
            ),
            TimeZone(
                code="UTC+1",
                name_cn="东一区",
                name_en="UTC+1",
                explaination="东一区 7.5° E～22.5° E 15° E",
            ),
            TimeZone(
                code="UTC+2",
                name_cn="东二区",
                name_en="UTC+2",
                explaination="东二区 22.5° E～37.5° E 30° E",
            ),
            TimeZone(
                code="UTC+3",
                name_cn="东三区",
                name_en="UTC+3",
                explaination="东三区 37.5° E～52.5° E 45° E",
            ),
            TimeZone(
                code="UTC+4",
                name_cn="东四区",
                name_en="UTC+4",
                explaination="东四区 52.5° E～67.5° E 60° E",
            ),
            TimeZone(
                code="UTC+5",
                name_cn="东五区",
                name_en="UTC+5",
                explaination="东五区 67.5° E～82.5° E 75° E",
            ),
            TimeZone(
                code="UTC+6",
                name_cn="东六区",
                name_en="UTC+6",
                explaination="东六区 82.5° E～97.5° E 90° E",
            ),
            TimeZone(
                code="UTC+7",
                name_cn="东七区",
                name_en="UTC+7",
                explaination="东七区 97.5° E～112.5° E 105° E",
            ),
            TimeZone(
                code="UTC+8",
                name_cn="东八区",
                name_en="UTC+8",
                explaination="东八区 112.5° E～127.5° E 120° E",
            ),
            TimeZone(
                code="UTC+9",
                name_cn="东九区",
                name_en="UTC+9",
                explaination="东九区 127.5° E～142.5° E 135° E",
            ),
            TimeZone(
                code="UTC+10",
                name_cn="东十区",
                name_en="UTC+10",
                explaination="东十区 142.5° E～157.5° E 150° E",
            ),
            TimeZone(
                code="UTC+11",
                name_cn="东十一区",
                name_en="UTC+11",
                explaination="东十一区 157.5° E～172.5° E 165° E",
            ),
            TimeZone(
                code="UTC+12",
                name_cn="东十二区",
                name_en="UTC+12",
                explaination="东十二区 172.5° E～180° E 180°",
            ),
            TimeZone(
                code="UTC-1",
                name_cn="西一区",
                name_en="UTC-1",
                explaination="西一区 7.5° W～22.5° W 15° W",
            ),
            TimeZone(
                code="UTC-2",
                name_cn="西二区",
                name_en="UTC-2",
                explaination="西二区 22.5° W～37.5° W 30° W",
            ),
            TimeZone(
                code="UTC-3",
                name_cn="西三区",
                name_en="UTC-3",
                explaination="西三区 37.5° W～52.5° W 45° W",
            ),
            TimeZone(
                code="UTC-4",
                name_cn="西四区",
                name_en="UTC-4",
                explaination="西四区 52.5° W～67.5° W 60° W",
            ),
            TimeZone(
                code="UTC-5",
                name_cn="西五区",
                name_en="UTC-5",
                explaination="西五区 67.5° W～82.5° W 75° W",
            ),
            TimeZone(
                code="UTC-6",
                name_cn="西六区",
                name_en="UTC-6",
                explaination="西六区 82.5° W～97.5° W 90° W",
            ),
            TimeZone(
                code="UTC-7",
                name_cn="西七区",
                name_en="UTC-7",
                explaination="西七区 97.5° W～112.5° W 105° W",
            ),
            TimeZone(
                code="UTC-8",
                name_cn="西八区",
                name_en="UTC-8",
                explaination="西八区 112.5° W～127.5° W 120° W",
            ),
            TimeZone(
                code="UTC-9",
                name_cn="西九区",
                name_en="UTC-9",
                explaination="西九区 127.5° W～142.5° W 135° W",
            ),
            TimeZone(
                code="UTC-10",
                name_cn="西十区",
                name_en="UTC-10",
                explaination="西十区 142.5° W～157.5° W 150° W",
            ),
            TimeZone(
                code="UTC-11",
                name_cn="西十一区",
                name_en="UTC-11",
                explaination="西十一区 157.5° W～172.5° W 165° W",
            ),
            TimeZone(
                code="UTC-12",
                name_cn="西十二区",
                name_en="UTC-12",
                explaination="西十二区 172.5° W～180° W 180°",
            ),
        ]

    def get_attributes(self) -> list[AttributeMapping]:
        """获取属性列表"""
        attributes = [
            AttributeMapping(attribute="speed_ground", description="对地航速"),
            AttributeMapping(attribute="speed_water", description="对水航速"),
            AttributeMapping(attribute="draft", description="船艏船尾平均吃水"),
            AttributeMapping(attribute="trim", description="船舶纵倾"),
            AttributeMapping(attribute="me_rpm", description="主机转速"),
            AttributeMapping(attribute="wind_speed", description="风速"),
            AttributeMapping(attribute="wind_direction", description="风向"),
        ]
        return attributes

    def get_attribute_mapping(self) -> list[AttributeMappings]:
        """获取属性组合列表"""
        mappings = [
            AttributeMappings(
                attribute_left=AttributeMapping(
                    attribute="speed_water", description="对水航速"
                ),
                attribute_right=AttributeMapping(
                    attribute="me_shaft_power", description="主机功率"
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(
                    attribute="speed_water", description="对水航速"
                ),
                attribute_right=AttributeMapping(
                    attribute="me_fuel_consumption_nmile",
                    description="主机每海里油耗（Kg/NM）",
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(
                    attribute="me_rpm", description="主机转速"
                ),
                attribute_right=AttributeMapping(
                    attribute="me_shaft_power", description="主机功率"
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(
                    attribute="me_rpm", description="主机转速"
                ),
                attribute_right=AttributeMapping(
                    attribute="me_fuel_consumption_kwh",
                    description="主机功率油耗（g/kWh）",
                ),
            ),
            AttributeMappings(
                attribute_left=AttributeMapping(
                    attribute="me_shaft_power", description="主机功率"
                ),
                attribute_right=AttributeMapping(
                    attribute="me_fuel_consumption_kwh",
                    description="主机功率油耗（g/kWh）",
                ),
            ),
        ]
        return mappings

    def get_fuel_type_categories(self) -> list[LabelValue]:
        category_list = [
            LabelValue(value="hfo", label="重油"),
            LabelValue(value="lfo", label="轻油"),
            LabelValue(value="mgo", label="船舶柴油"),
            LabelValue(value="mdo", label="内河船用燃料油"),
            LabelValue(value="lng", label="液化天然气"),
            LabelValue(value="lpg_p", label="液化石油气(丙烷)"),
            LabelValue(value="lpg_b", label="液化石油气(丁烷)"),
            LabelValue(value="methanol", label="甲醇"),
            LabelValue(value="ethanol", label="乙醇"),
            LabelValue(value="ethane", label="乙烷"),
            LabelValue(value="ammonia", label="氨"),
            LabelValue(value="hydrogen", label="氢"),
        ]
        return category_list
