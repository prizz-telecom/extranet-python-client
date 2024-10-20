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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from prizz_extranet.models.process_attributes_messages import ProcessAttributesMessages
from prizz_extranet.models.process_attributes_qualification import ProcessAttributesQualification
from typing import Optional, Set
from typing_extensions import Self

class ProcessAttributes(BaseModel):
    """
    ProcessAttributes
    """ # noqa: E501
    verif_cablage_ok: Optional[StrictBool] = None
    etat_voyants: Optional[StrictStr] = None
    qualification: Optional[ProcessAttributesQualification] = None
    customer_mails: Optional[List[StrictStr]] = None
    messages: Optional[ProcessAttributesMessages] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["verif_cablage_ok", "etat_voyants", "qualification", "customer_mails", "messages"]

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
        """Create an instance of ProcessAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of qualification
        if self.qualification:
            _dict['qualification'] = self.qualification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if verif_cablage_ok (nullable) is None
        # and model_fields_set contains the field
        if self.verif_cablage_ok is None and "verif_cablage_ok" in self.model_fields_set:
            _dict['verif_cablage_ok'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProcessAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "verif_cablage_ok": obj.get("verif_cablage_ok"),
            "etat_voyants": obj.get("etat_voyants"),
            "qualification": ProcessAttributesQualification.from_dict(obj["qualification"]) if obj.get("qualification") is not None else None,
            "customer_mails": obj.get("customer_mails"),
            "messages": ProcessAttributesMessages.from_dict(obj["messages"]) if obj.get("messages") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


