# coding: utf-8

"""
    Prizz-Telecom Extranet API

    Prizz-Telecom Extranet API https://dev.prizz-telecom.fr/

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from prizz_extranet.models.product_group import ProductGroup
from typing import Optional, Set
from typing_extensions import Self

class Product(BaseModel):
    """
    Product
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    attributes: Optional[Dict[str, Any]] = None
    product_code: Optional[StrictStr] = Field(default=None, alias="productCode")
    group: Optional[ProductGroup] = None
    __properties: ClassVar[List[str]] = ["id", "name", "attributes", "productCode", "group"]

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
        """Create an instance of Product from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "attributes": obj.get("attributes"),
            "productCode": obj.get("productCode"),
            "group": ProductGroup.from_dict(obj["group"]) if obj.get("group") is not None else None
        })
        return _obj


