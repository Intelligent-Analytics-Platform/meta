"""
通用响应模型
"""

from typing import Generic, TypeVar

from pydantic import BaseModel

# 定义泛型类型变量
T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    """
    通用API响应模型
    """

    code: int = 200
    message: str = "操作成功"
    data: T | None = None


class LabelValue(BaseModel):
    """
    标签值对模型，用于下拉框等场景
    """

    label: str
    value: str | int
