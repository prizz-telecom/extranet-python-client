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
from prizz_extranet.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class UserRole(BaseModel):
    """
    UserRole
    """ # noqa: E501
    available_workflows: Optional[List[StrictStr]] = Field(default=None, description="liste des processus disponible pour l'objet", alias="availableWorkflows")
    id: Optional[StrictInt] = None
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    last_modified_date: Optional[datetime] = Field(default=None, alias="lastModifiedDate")
    user: Optional[User] = None
    role: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["availableWorkflows", "id", "createDate", "lastModifiedDate", "user", "role"]

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
        """Create an instance of UserRole from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if last_modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_date is None and "last_modified_date" in self.model_fields_set:
            _dict['lastModifiedDate'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableWorkflows": obj.get("availableWorkflows"),
            "id": obj.get("id"),
            "createDate": obj.get("createDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "user": User.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "role": obj.get("role")
        })
        return _obj


