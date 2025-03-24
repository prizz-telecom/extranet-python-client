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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AddCommercialOfferComment(BaseModel):
    """
    AddCommercialOfferComment
    """ # noqa: E501
    title: Optional[StrictStr] = None
    thread_id: Optional[StrictInt] = Field(default=None, alias="threadId")
    parent_id: Optional[StrictInt] = Field(default=None, alias="parentId")
    content_type: Optional[StrictStr] = Field(default=None, alias="contentType")
    content: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["title", "threadId", "parentId", "contentType", "content"]

    @field_validator('content_type')
    def content_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['text', 'markdown']):
            raise ValueError("must be one of enum values ('text', 'markdown')")
        return value

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
        """Create an instance of AddCommercialOfferComment from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if thread_id (nullable) is None
        # and model_fields_set contains the field
        if self.thread_id is None and "thread_id" in self.model_fields_set:
            _dict['threadId'] = None

        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parentId'] = None

        # set to None if content_type (nullable) is None
        # and model_fields_set contains the field
        if self.content_type is None and "content_type" in self.model_fields_set:
            _dict['contentType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddCommercialOfferComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "threadId": obj.get("threadId"),
            "parentId": obj.get("parentId"),
            "contentType": obj.get("contentType"),
            "content": obj.get("content")
        })
        return _obj


