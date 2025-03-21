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
from typing import Optional, Set
from typing_extensions import Self

class Contact(BaseModel):
    """
    Contact
    """ # noqa: E501
    available_workflows: Optional[List[StrictStr]] = Field(default=None, description="liste des processus disponible pour l'objet", alias="availableWorkflows")
    id: Optional[StrictInt] = None
    firstname: Optional[StrictStr] = None
    lastname: Optional[StrictStr] = None
    company_name: Optional[StrictStr] = Field(default=None, alias="companyName")
    email: Optional[StrictStr] = None
    phone1: Optional[StrictStr] = None
    phone2: Optional[StrictStr] = None
    gender: Optional[StrictStr] = None
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    last_modified_date: Optional[datetime] = Field(default=None, alias="lastModifiedDate")
    __properties: ClassVar[List[str]] = ["availableWorkflows", "id", "firstname", "lastname", "companyName", "email", "phone1", "phone2", "gender", "createDate", "lastModifiedDate"]

    @field_validator('available_workflows')
    def available_workflows_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Submit\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Sign\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Rename\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RenameSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateOfferItemInOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\SetOffer\\Context', 'Infracorp\\Services\\Workflow\\Comment\\AddComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\SubscribeThread\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateThread\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Invoice\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Users\\CreateToken\\Context', 'Infracorp\\Services\\Workflow\\Users\\RevokeToken\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSubscribers\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSectionItems\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntityContact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Contact\\Update\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateDescription\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateClientRef\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Activation\\SetupL2\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateClientRefSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Users\\SwitchActiveRole\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddUserRole\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\MigrateCoaxToL2Premium\\Context']):
                raise ValueError("each list item must be one of ('Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Submit\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Sign\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Rename\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RenameSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateOfferItemInOffer\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\SetOffer\\Context', 'Infracorp\\Services\\Workflow\\Comment\\AddComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\SubscribeThread\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateComment\\Context', 'Infracorp\\Services\\Workflow\\Comment\\UpdateThread\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Invoice\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\CreateCommentThread\\Context', 'Infracorp\\Services\\Workflow\\Users\\CreateToken\\Context', 'Infracorp\\Services\\Workflow\\Users\\RevokeToken\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSubscribers\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AddItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\RemoveItem\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateSectionItems\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddContact\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntityContact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Contact\\Update\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateDescription\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\UpdateClientRef\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Activation\\SetupL2\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\UpdateClientRefSection\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\AssignContact\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\CommercialOffer\\Contact\\SwitchActive\\Context', 'Infracorp\\Services\\Workflow\\Users\\SwitchActiveRole\\Context', 'Infracorp\\Services\\Workflow\\ClientLegalEntity\\AddUserRole\\Context', 'Infracorp\\Services\\Workflow\\ServiceContract\\MigrateCoaxToL2Premium\\Context')")
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
        """Create an instance of Contact from a JSON string"""
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
        # set to None if firstname (nullable) is None
        # and model_fields_set contains the field
        if self.firstname is None and "firstname" in self.model_fields_set:
            _dict['firstname'] = None

        # set to None if company_name (nullable) is None
        # and model_fields_set contains the field
        if self.company_name is None and "company_name" in self.model_fields_set:
            _dict['companyName'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if phone1 (nullable) is None
        # and model_fields_set contains the field
        if self.phone1 is None and "phone1" in self.model_fields_set:
            _dict['phone1'] = None

        # set to None if phone2 (nullable) is None
        # and model_fields_set contains the field
        if self.phone2 is None and "phone2" in self.model_fields_set:
            _dict['phone2'] = None

        # set to None if gender (nullable) is None
        # and model_fields_set contains the field
        if self.gender is None and "gender" in self.model_fields_set:
            _dict['gender'] = None

        # set to None if last_modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_date is None and "last_modified_date" in self.model_fields_set:
            _dict['lastModifiedDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Contact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableWorkflows": obj.get("availableWorkflows"),
            "id": obj.get("id"),
            "firstname": obj.get("firstname"),
            "lastname": obj.get("lastname"),
            "companyName": obj.get("companyName"),
            "email": obj.get("email"),
            "phone1": obj.get("phone1"),
            "phone2": obj.get("phone2"),
            "gender": obj.get("gender"),
            "createDate": obj.get("createDate"),
            "lastModifiedDate": obj.get("lastModifiedDate")
        })
        return _obj


