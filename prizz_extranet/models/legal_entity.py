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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class LegalEntity(BaseModel):
    """
    LegalEntity
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    house_number: Optional[StrictInt] = Field(default=None, alias="houseNumber")
    house_number_complement: Optional[StrictStr] = Field(default=None, alias="houseNumberComplement")
    street_name: Optional[StrictStr] = Field(default=None, alias="streetName")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    city_name: Optional[StrictStr] = Field(default=None, alias="cityName")
    insee_code: Optional[StrictStr] = Field(default=None, alias="inseeCode")
    url: Optional[StrictStr] = None
    num_vat_intracommunity: Optional[StrictStr] = Field(default=None, alias="numVatIntracommunity")
    siren: Optional[StrictStr] = None
    code_ape: Optional[StrictStr] = Field(default=None, alias="codeApe")
    rcs: Optional[StrictStr] = None
    tel: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    x: Optional[Union[StrictFloat, StrictInt]] = None
    y: Optional[Union[StrictFloat, StrictInt]] = None
    projection: Optional[StrictStr] = None
    logo: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "name", "houseNumber", "houseNumberComplement", "streetName", "postalCode", "cityName", "inseeCode", "url", "numVatIntracommunity", "siren", "codeApe", "rcs", "tel", "email", "latitude", "longitude", "x", "y", "projection", "logo"]

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
        """Create an instance of LegalEntity from a JSON string"""
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
        # set to None if house_number (nullable) is None
        # and model_fields_set contains the field
        if self.house_number is None and "house_number" in self.model_fields_set:
            _dict['houseNumber'] = None

        # set to None if house_number_complement (nullable) is None
        # and model_fields_set contains the field
        if self.house_number_complement is None and "house_number_complement" in self.model_fields_set:
            _dict['houseNumberComplement'] = None

        # set to None if street_name (nullable) is None
        # and model_fields_set contains the field
        if self.street_name is None and "street_name" in self.model_fields_set:
            _dict['streetName'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postalCode'] = None

        # set to None if city_name (nullable) is None
        # and model_fields_set contains the field
        if self.city_name is None and "city_name" in self.model_fields_set:
            _dict['cityName'] = None

        # set to None if insee_code (nullable) is None
        # and model_fields_set contains the field
        if self.insee_code is None and "insee_code" in self.model_fields_set:
            _dict['inseeCode'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if num_vat_intracommunity (nullable) is None
        # and model_fields_set contains the field
        if self.num_vat_intracommunity is None and "num_vat_intracommunity" in self.model_fields_set:
            _dict['numVatIntracommunity'] = None

        # set to None if siren (nullable) is None
        # and model_fields_set contains the field
        if self.siren is None and "siren" in self.model_fields_set:
            _dict['siren'] = None

        # set to None if code_ape (nullable) is None
        # and model_fields_set contains the field
        if self.code_ape is None and "code_ape" in self.model_fields_set:
            _dict['codeApe'] = None

        # set to None if rcs (nullable) is None
        # and model_fields_set contains the field
        if self.rcs is None and "rcs" in self.model_fields_set:
            _dict['rcs'] = None

        # set to None if tel (nullable) is None
        # and model_fields_set contains the field
        if self.tel is None and "tel" in self.model_fields_set:
            _dict['tel'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if x (nullable) is None
        # and model_fields_set contains the field
        if self.x is None and "x" in self.model_fields_set:
            _dict['x'] = None

        # set to None if y (nullable) is None
        # and model_fields_set contains the field
        if self.y is None and "y" in self.model_fields_set:
            _dict['y'] = None

        # set to None if projection (nullable) is None
        # and model_fields_set contains the field
        if self.projection is None and "projection" in self.model_fields_set:
            _dict['projection'] = None

        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LegalEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "houseNumber": obj.get("houseNumber"),
            "houseNumberComplement": obj.get("houseNumberComplement"),
            "streetName": obj.get("streetName"),
            "postalCode": obj.get("postalCode"),
            "cityName": obj.get("cityName"),
            "inseeCode": obj.get("inseeCode"),
            "url": obj.get("url"),
            "numVatIntracommunity": obj.get("numVatIntracommunity"),
            "siren": obj.get("siren"),
            "codeApe": obj.get("codeApe"),
            "rcs": obj.get("rcs"),
            "tel": obj.get("tel"),
            "email": obj.get("email"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "x": obj.get("x"),
            "y": obj.get("y"),
            "projection": obj.get("projection"),
            "logo": obj.get("logo")
        })
        return _obj


