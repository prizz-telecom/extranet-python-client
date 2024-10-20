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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CommercialOfferSearch(BaseModel):
    """
    CommercialOfferSearch
    """ # noqa: E501
    index: Optional[StrictStr] = None
    query: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    legal_entity_id: Optional[StrictStr] = Field(default=None, alias="legalEntityId")
    client_legal_entity_id: Optional[StrictStr] = Field(default=None, alias="clientLegalEntityId")
    name: Optional[StrictStr] = None
    notes: Optional[StrictStr] = None
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    section_names: Optional[StrictStr] = Field(default=None, alias="sectionNames")
    addresses: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["index", "query", "id", "legalEntityId", "clientLegalEntityId", "name", "notes", "createDate", "sectionNames", "addresses"]

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
        """Create an instance of CommercialOfferSearch from a JSON string"""
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
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if create_date (nullable) is None
        # and model_fields_set contains the field
        if self.create_date is None and "create_date" in self.model_fields_set:
            _dict['createDate'] = None

        # set to None if section_names (nullable) is None
        # and model_fields_set contains the field
        if self.section_names is None and "section_names" in self.model_fields_set:
            _dict['sectionNames'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommercialOfferSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "index": obj.get("index"),
            "query": obj.get("query"),
            "id": obj.get("id"),
            "legalEntityId": obj.get("legalEntityId"),
            "clientLegalEntityId": obj.get("clientLegalEntityId"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "createDate": obj.get("createDate"),
            "sectionNames": obj.get("sectionNames"),
            "addresses": obj.get("addresses")
        })
        return _obj


