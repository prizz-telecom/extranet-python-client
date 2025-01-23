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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from prizz_extranet.models.client_contract import ClientContract
from prizz_extranet.models.contact import Contact
from prizz_extranet.models.typed_contact import TypedContact
from prizz_extranet.models.user_role import UserRole
from typing import Optional, Set
from typing_extensions import Self

class ClientLegalEntity(BaseModel):
    """
    ClientLegalEntity
    """ # noqa: E501
    available_workflows: Optional[List[StrictStr]] = Field(default=None, description="liste des processus disponible pour l'objet", alias="availableWorkflows")
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
    arcep_code: Optional[StrictStr] = Field(default=None, alias="arcepCode")
    contacts: Optional[List[Contact]] = None
    configured_contacts: Optional[List[TypedContact]] = Field(default=None, alias="configuredContacts")
    contracts: Optional[List[ClientContract]] = None
    roles: Optional[List[UserRole]] = None
    __properties: ClassVar[List[str]] = ["availableWorkflows", "id", "name", "houseNumber", "houseNumberComplement", "streetName", "postalCode", "cityName", "inseeCode", "url", "numVatIntracommunity", "siren", "codeApe", "rcs", "tel", "email", "latitude", "longitude", "x", "y", "projection", "arcepCode", "contacts", "configuredContacts", "contracts", "roles"]

    @field_validator('available_workflows')
    def available_workflows_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Submit\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Sign\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Rename\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RenameSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateOfferItemInOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\SetOffer\\Context', 'Infracorp\\Services\\Workflow\\Comment\\AddComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\SubscribeThread\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateThread\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Invoice\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Users\\CreateToken\\Context', 'Infracorp\\Services\\Workflow\\Users\\RevokeToken\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSubscribers\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSectionItems\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntityContact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Contact\\Update\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateDescription\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateClientRef\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Activation\\SetupL2\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateClientRefSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Users\\SwitchActiveRole\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddUserRole\\Context']):
                raise ValueError("each list item must be one of ('Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Submit\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Sign\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Rename\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RenameSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateOfferItemInOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\SetOffer\\Context', 'Infracorp\\Services\\Workflow\\Comment\\AddComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\SubscribeThread\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateThread\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Invoice\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Users\\CreateToken\\Context', 'Infracorp\\Services\\Workflow\\Users\\RevokeToken\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSubscribers\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSectionItems\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntityContact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Contact\\Update\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateDescription\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateClientRef\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Activation\\SetupL2\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateClientRefSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Users\\SwitchActiveRole\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddUserRole\\Context')")
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
        """Create an instance of ClientLegalEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in configured_contacts (list)
        _items = []
        if self.configured_contacts:
            for _item_configured_contacts in self.configured_contacts:
                if _item_configured_contacts:
                    _items.append(_item_configured_contacts.to_dict())
            _dict['configuredContacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in contracts (list)
        _items = []
        if self.contracts:
            for _item_contracts in self.contracts:
                if _item_contracts:
                    _items.append(_item_contracts.to_dict())
            _dict['contracts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item_roles in self.roles:
                if _item_roles:
                    _items.append(_item_roles.to_dict())
            _dict['roles'] = _items
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

        # set to None if arcep_code (nullable) is None
        # and model_fields_set contains the field
        if self.arcep_code is None and "arcep_code" in self.model_fields_set:
            _dict['arcepCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientLegalEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableWorkflows": obj.get("availableWorkflows"),
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
            "arcepCode": obj.get("arcepCode"),
            "contacts": [Contact.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None,
            "configuredContacts": [TypedContact.from_dict(_item) for _item in obj["configuredContacts"]] if obj.get("configuredContacts") is not None else None,
            "contracts": [ClientContract.from_dict(_item) for _item in obj["contracts"]] if obj.get("contracts") is not None else None,
            "roles": [UserRole.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None
        })
        return _obj


