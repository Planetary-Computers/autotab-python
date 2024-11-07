# coding: utf-8

"""
    Autotab API

    AI that does your repetitive work end to end, with superhuman reliability.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class VariableDataType(str, Enum):
    """
    VariableDataType
    """

    """
    allowed enum values
    """
    STRING = 'string'
    NUMBER = 'number'
    BOOLEAN = 'boolean'
    ARRAY = 'array'
    OBJECT = 'object'
    FILE = 'file'
    TAB = 'tab'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VariableDataType from a JSON string"""
        return cls(json.loads(json_str))


