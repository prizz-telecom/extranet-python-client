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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RunningProcess(BaseModel):
    """
    RunningProcess
    """ # noqa: E501
    id: Optional[StrictInt] = None
    lib: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    status_code: Optional[StrictInt] = None
    create_date: Optional[StrictStr] = None
    process_class: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "lib", "state", "status_code", "create_date", "process_class"]

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
        """Create an instance of RunningProcess from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if lib (nullable) is None
        # and model_fields_set contains the field
        if self.lib is None and "lib" in self.model_fields_set:
            _dict['lib'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['status_code'] = None

        # set to None if process_class (nullable) is None
        # and model_fields_set contains the field
        if self.process_class is None and "process_class" in self.model_fields_set:
            _dict['process_class'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunningProcess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "lib": obj.get("lib"),
            "state": obj.get("state"),
            "status_code": obj.get("status_code"),
            "create_date": obj.get("create_date"),
            "process_class": obj.get("process_class")
        })
        return _obj

