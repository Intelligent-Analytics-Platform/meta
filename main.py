from fastapi import Depends, FastAPI

from model.attribute_mapping import AttributeMapping, AttributeMappings
from model.fuel_type import FuelType
from model.label_value import LabelValue
from model.response import ResponseModel
from model.ship_type import ShipType
from model.time_zone import TimeZone
from service import MetaService, get_meta_service

api = FastAPI(title="Meta API", description="数据元数据管理系统", version="0.1.0")


@api.get("/")
async def root():
    """根路径"""
    return {"status": "healthy", "service": "Meta Application API", "version": "0.1.0"}


@api.get(
    "/fuel_type", summary="获取燃料类型", response_model=ResponseModel[list[FuelType]]
)
async def get_fuel_types(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[FuelType]]:
    """
    "新增船舶"弹窗，选择设备燃料类型
    """
    fuel_types = service.get_all_fuel_types()
    return ResponseModel(code=200, data=fuel_types, message="获取燃料类型成功")


@api.get(
    "/ship_type", summary="获取船舶类型", response_model=ResponseModel[list[ShipType]]
)
async def get_ship_types(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[ShipType]]:
    """
    "新增船舶"弹窗，选择船舶类型
    """
    ship_types = service.get_all_ship_types()
    return ResponseModel(code=200, data=ship_types, message="获取船舶类型成功")


@api.get("/time_zone", summary="获取时区", response_model=ResponseModel[list[TimeZone]])
async def get_time_zones(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[TimeZone]]:
    """
    "新增船舶"弹窗，选择船用时区
    """
    time_zones = service.get_all_time_zones()
    return ResponseModel(code=200, data=time_zones, message="获取时区成功")


@api.get(
    "/attributes", summary="属性", response_model=ResponseModel[list[AttributeMapping]]
)
async def get_attributes(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[AttributeMapping]]:
    """
    "数据分析与回放"页面属性选择下拉框可选项
    """
    attributes = service.get_attributes()
    return ResponseModel(code=200, data=attributes, message="获取属性成功")


@api.get(
    "/attribute_mapping",
    summary="属性组合",
    response_model=ResponseModel[list[AttributeMappings]],
)
async def get_attribute_mapping(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[AttributeMappings]]:
    """
    多角度展示页面，选择属性组合
    """
    mappings = service.get_attribute_mapping()
    return ResponseModel(code=200, data=mappings, message="获取属性组合成功")


@api.get(
    "/fuel_type_category",
    summary="燃料类型分类",
    response_model=ResponseModel[list[LabelValue]],
)
async def get_fuel_type_category(
    service: MetaService = Depends(get_meta_service),
) -> ResponseModel[list[LabelValue]]:
    """
    能耗统计页面，选择燃料类型分类
    """
    categories = service.get_fuel_type_categories()
    return ResponseModel(code=200, data=categories, message="获取燃料类型分类成功")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(api, host="0.0.0.0", port=8001)
