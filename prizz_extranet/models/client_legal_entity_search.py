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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from prizz_extranet.models.contact_search import ContactSearch
from typing import Optional, Set
from typing_extensions import Self

class ClientLegalEntitySearch(BaseModel):
    """
    ClientLegalEntitySearch
    """ # noqa: E501
    index: Optional[StrictStr] = None
    query: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    legal_entity_ids: Optional[List[StrictStr]] = Field(default=None, alias="legalEntityIds")
    name: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    siren: Optional[StrictStr] = None
    tel: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    contacts: Optional[List[ContactSearch]] = None
    __properties: ClassVar[List[str]] = ["index", "query", "id", "legalEntityIds", "name", "address", "siren", "tel", "email", "contacts"]

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
        """Create an instance of ClientLegalEntitySearch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contacts (list)
        _items = []
        if self.contacts:
            for _item_contacts in self.contacts:
                if _item_contacts:
                    _items.append(_item_contacts.to_dict())
            _dict['contacts'] = _items
        # set to None if siren (nullable) is None
        # and model_fields_set contains the field
        if self.siren is None and "siren" in self.model_fields_set:
            _dict['siren'] = None

        # set to None if tel (nullable) is None
        # and model_fields_set contains the field
        if self.tel is None and "tel" in self.model_fields_set:
            _dict['tel'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientLegalEntitySearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "index": obj.get("index"),
            "query": obj.get("query"),
            "id": obj.get("id"),
            "legalEntityIds": obj.get("legalEntityIds"),
            "name": obj.get("name"),
            "address": obj.get("address"),
            "siren": obj.get("siren"),
            "tel": obj.get("tel"),
            "email": obj.get("email"),
            "contacts": [ContactSearch.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None
        })
        return _obj


