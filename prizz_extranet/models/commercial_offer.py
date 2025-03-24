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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from prizz_extranet.models.client_legal_entity import ClientLegalEntity
from prizz_extranet.models.commercial_offer_section import CommercialOfferSection
from prizz_extranet.models.commercial_offer_vat_detail_inner import CommercialOfferVatDetailInner
from prizz_extranet.models.commercial_offer_vat_detail_str_inner import CommercialOfferVatDetailStrInner
from prizz_extranet.models.contact import Contact
from prizz_extranet.models.legal_entity import LegalEntity
from prizz_extranet.models.typed_contact import TypedContact
from typing import Optional, Set
from typing_extensions import Self

class CommercialOffer(BaseModel):
    """
    CommercialOffer
    """ # noqa: E501
    available_workflows: Optional[List[StrictStr]] = Field(default=None, description="liste des processus disponible pour l'objet", alias="availableWorkflows")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    last_modified_date: Optional[datetime] = Field(default=None, alias="lastModifiedDate")
    notes: Optional[StrictStr] = None
    rc_total: Optional[Dict[str, StrictInt]] = Field(default=None, alias="rcTotal")
    rc_total_str: Optional[Dict[str, StrictStr]] = Field(default=None, alias="rcTotalStr")
    rc_vat_total: Optional[Dict[str, StrictInt]] = Field(default=None, alias="rcVATTotal")
    rc_vat_total_str: Optional[Dict[str, StrictStr]] = Field(default=None, alias="rcVATTotalStr")
    nrc_total: Optional[StrictInt] = Field(default=None, alias="nrcTotal")
    nrc_total_str: Optional[StrictStr] = Field(default=None, alias="nrcTotalStr")
    nrc_vat_total: Optional[StrictInt] = Field(default=None, alias="nrcVATTotal")
    nrc_vat_total_str: Optional[StrictStr] = Field(default=None, alias="nrcVATTotalStr")
    status: Optional[StrictStr] = None
    legal_entity: Optional[LegalEntity] = Field(default=None, alias="legalEntity")
    client_legal_entity: Optional[ClientLegalEntity] = Field(default=None, alias="clientLegalEntity")
    sign_date: Optional[datetime] = Field(default=None, alias="signDate")
    submit_date: Optional[datetime] = Field(default=None, alias="submitDate")
    delivery_delay: Optional[StrictInt] = Field(default=None, alias="deliveryDelay")
    total: Optional[StrictInt] = None
    total_str: Optional[StrictStr] = Field(default=None, alias="totalStr")
    vat_total: Optional[StrictInt] = Field(default=None, alias="vatTotal")
    vat_total_str: Optional[StrictStr] = Field(default=None, alias="vatTotalStr")
    section_names: Optional[StrictStr] = Field(default=None, alias="sectionNames")
    vat_detail: Optional[List[CommercialOfferVatDetailInner]] = Field(default=None, alias="vatDetail")
    vat_detail_str: Optional[List[CommercialOfferVatDetailStrInner]] = Field(default=None, alias="vatDetailStr")
    sections: Optional[List[CommercialOfferSection]] = None
    contacts: Optional[List[Contact]] = None
    configured_contacts: Optional[List[TypedContact]] = Field(default=None, alias="configuredContacts")
    __properties: ClassVar[List[str]] = ["availableWorkflows", "id", "name", "createDate", "lastModifiedDate", "notes", "rcTotal", "rcTotalStr", "rcVATTotal", "rcVATTotalStr", "nrcTotal", "nrcTotalStr", "nrcVATTotal", "nrcVATTotalStr", "status", "legalEntity", "clientLegalEntity", "signDate", "submitDate", "deliveryDelay", "total", "totalStr", "vatTotal", "vatTotalStr", "sectionNames", "vatDetail", "vatDetailStr", "sections", "contacts", "configuredContacts"]

    @field_validator('available_workflows')
    def available_workflows_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Submit\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Sign\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Rename\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RenameSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateOfferItemInOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\SetOffer\\Context', 'Infracorp\\Services\\Workflow\\Comment\\AddComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\SubscribeThread\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateThread\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Invoice\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Users\\CreateToken\\Context', 'Infracorp\\Services\\Workflow\\Users\\RevokeToken\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSubscribers\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSectionItems\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntityContact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Contact\\Update\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateDescription\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateClientRef\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Activation\\SetupL2\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateClientRefSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Users\\SwitchActiveRole\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddUserRole\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\ChangeContact\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\CustomerCancel\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\CustomerChangeDate\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\CustomerConfirm\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\MigrateCoaxToL2Premium\\Context']):
                raise ValueError("each list item must be one of ('Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Submit\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Sign\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Rename\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RenameSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateOfferItemInOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\SetOffer\\Context', 'Infracorp\\Services\\Workflow\\Comment\\AddComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\SubscribeThread\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateThread\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Invoice\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Users\\CreateToken\\Context', 'Infracorp\\Services\\Workflow\\Users\\RevokeToken\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSubscribers\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSectionItems\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntityContact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Contact\\Update\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateDescription\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateClientRef\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Activation\\SetupL2\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateClientRefSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Users\\SwitchActiveRole\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddUserRole\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\ChangeContact\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\CustomerCancel\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\CustomerChangeDate\\Context', 'Infracorp\\Services\\Workflow\\Appointment\\CustomerConfirm\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\MigrateCoaxToL2Premium\\Context')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['new', 'estimate_pending', 'approval_pending', 'validated', 'abandoned', 'signed']):
            raise ValueError("must be one of enum values ('new', 'estimate_pending', 'approval_pending', 'validated', 'abandoned', 'signed')")
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
        """Create an instance of CommercialOffer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of legal_entity
        if self.legal_entity:
            _dict['legalEntity'] = self.legal_entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_legal_entity
        if self.client_legal_entity:
            _dict['clientLegalEntity'] = self.client_legal_entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vat_detail (list)
        _items = []
        if self.vat_detail:
            for _item_vat_detail in self.vat_detail:
                if _item_vat_detail:
                    _items.append(_item_vat_detail.to_dict())
            _dict['vatDetail'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vat_detail_str (list)
        _items = []
        if self.vat_detail_str:
            for _item_vat_detail_str in self.vat_detail_str:
                if _item_vat_detail_str:
                    _items.append(_item_vat_detail_str.to_dict())
            _dict['vatDetailStr'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sections (list)
        _items = []
        if self.sections:
            for _item_sections in self.sections:
                if _item_sections:
                    _items.append(_item_sections.to_dict())
            _dict['sections'] = _items
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
        # set to None if last_modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_date is None and "last_modified_date" in self.model_fields_set:
            _dict['lastModifiedDate'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if nrc_total (nullable) is None
        # and model_fields_set contains the field
        if self.nrc_total is None and "nrc_total" in self.model_fields_set:
            _dict['nrcTotal'] = None

        # set to None if nrc_vat_total (nullable) is None
        # and model_fields_set contains the field
        if self.nrc_vat_total is None and "nrc_vat_total" in self.model_fields_set:
            _dict['nrcVATTotal'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if sign_date (nullable) is None
        # and model_fields_set contains the field
        if self.sign_date is None and "sign_date" in self.model_fields_set:
            _dict['signDate'] = None

        # set to None if submit_date (nullable) is None
        # and model_fields_set contains the field
        if self.submit_date is None and "submit_date" in self.model_fields_set:
            _dict['submitDate'] = None

        # set to None if delivery_delay (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_delay is None and "delivery_delay" in self.model_fields_set:
            _dict['deliveryDelay'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if vat_total (nullable) is None
        # and model_fields_set contains the field
        if self.vat_total is None and "vat_total" in self.model_fields_set:
            _dict['vatTotal'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommercialOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableWorkflows": obj.get("availableWorkflows"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "createDate": obj.get("createDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "notes": obj.get("notes"),
            "rcTotal": obj.get("rcTotal"),
            "rcTotalStr": obj.get("rcTotalStr"),
            "rcVATTotal": obj.get("rcVATTotal"),
            "rcVATTotalStr": obj.get("rcVATTotalStr"),
            "nrcTotal": obj.get("nrcTotal"),
            "nrcTotalStr": obj.get("nrcTotalStr"),
            "nrcVATTotal": obj.get("nrcVATTotal"),
            "nrcVATTotalStr": obj.get("nrcVATTotalStr"),
            "status": obj.get("status"),
            "legalEntity": LegalEntity.from_dict(obj["legalEntity"]) if obj.get("legalEntity") is not None else None,
            "clientLegalEntity": ClientLegalEntity.from_dict(obj["clientLegalEntity"]) if obj.get("clientLegalEntity") is not None else None,
            "signDate": obj.get("signDate"),
            "submitDate": obj.get("submitDate"),
            "deliveryDelay": obj.get("deliveryDelay"),
            "total": obj.get("total"),
            "totalStr": obj.get("totalStr"),
            "vatTotal": obj.get("vatTotal"),
            "vatTotalStr": obj.get("vatTotalStr"),
            "sectionNames": obj.get("sectionNames"),
            "vatDetail": [CommercialOfferVatDetailInner.from_dict(_item) for _item in obj["vatDetail"]] if obj.get("vatDetail") is not None else None,
            "vatDetailStr": [CommercialOfferVatDetailStrInner.from_dict(_item) for _item in obj["vatDetailStr"]] if obj.get("vatDetailStr") is not None else None,
            "sections": [CommercialOfferSection.from_dict(_item) for _item in obj["sections"]] if obj.get("sections") is not None else None,
            "contacts": [Contact.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None,
            "configuredContacts": [TypedContact.from_dict(_item) for _item in obj["configuredContacts"]] if obj.get("configuredContacts") is not None else None
        })
        return _obj


