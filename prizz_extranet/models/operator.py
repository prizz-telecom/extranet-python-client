# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Operator(BaseModel):
    """
    Operator
    """ # noqa: E501
    code: Optional[StrictStr] = None
    lib: Optional[StrictStr] = None
    delivery_doors: Optional[List[Any]] = None
    hosting_items: Optional[List[Any]] = None
    l2_services: Optional[List[Any]] = None
    fon_services: Optional[List[Any]] = None
    acces_internet_services: Optional[List[Any]] = None
    __properties: ClassVar[List[str]] = ["code", "lib", "delivery_doors", "hosting_items", "l2_services", "fon_services", "acces_internet_services"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Operator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if lib (nullable) is None
        # and model_fields_set contains the field
        if self.lib is None and "lib" in self.model_fields_set:
            _dict['lib'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Operator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "lib": obj.get("lib"),
            "delivery_doors": obj.get("delivery_doors"),
            "hosting_items": obj.get("hosting_items"),
            "l2_services": obj.get("l2_services"),
            "fon_services": obj.get("fon_services"),
            "acces_internet_services": obj.get("acces_internet_services")
        })
        return _obj


