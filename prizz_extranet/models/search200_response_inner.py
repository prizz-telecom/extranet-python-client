# coding: utf-8

"""
    Prizz-Telecom Extranet API

    Prizz-Telecom Extranet API https://dev.prizz-telecom.fr/

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from prizz_extranet.models.client_legal_entity_search import ClientLegalEntitySearch
from prizz_extranet.models.commercial_offer_search import CommercialOfferSearch
from prizz_extranet.models.invoice_search import InvoiceSearch
from prizz_extranet.models.service_contract_search import ServiceContractSearch
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

SEARCH200RESPONSEINNER_ANY_OF_SCHEMAS = ["ClientLegalEntitySearch", "CommercialOfferSearch", "InvoiceSearch", "ServiceContractSearch"]

class Search200ResponseInner(BaseModel):
    """
    Search200ResponseInner
    """

    # data type: ClientLegalEntitySearch
    anyof_schema_1_validator: Optional[ClientLegalEntitySearch] = None
    # data type: InvoiceSearch
    anyof_schema_2_validator: Optional[InvoiceSearch] = None
    # data type: CommercialOfferSearch
    anyof_schema_3_validator: Optional[CommercialOfferSearch] = None
    # data type: ServiceContractSearch
    anyof_schema_4_validator: Optional[ServiceContractSearch] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[ClientLegalEntitySearch, CommercialOfferSearch, InvoiceSearch, ServiceContractSearch]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "ClientLegalEntitySearch", "CommercialOfferSearch", "InvoiceSearch", "ServiceContractSearch" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = Search200ResponseInner.model_construct()
        error_messages = []
        # validate data type: ClientLegalEntitySearch
        if not isinstance(v, ClientLegalEntitySearch):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ClientLegalEntitySearch`")
        else:
            return v

        # validate data type: InvoiceSearch
        if not isinstance(v, InvoiceSearch):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InvoiceSearch`")
        else:
            return v

        # validate data type: CommercialOfferSearch
        if not isinstance(v, CommercialOfferSearch):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CommercialOfferSearch`")
        else:
            return v

        # validate data type: ServiceContractSearch
        if not isinstance(v, ServiceContractSearch):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ServiceContractSearch`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Search200ResponseInner with anyOf schemas: ClientLegalEntitySearch, CommercialOfferSearch, InvoiceSearch, ServiceContractSearch. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ClientLegalEntitySearch] = None
        try:
            instance.actual_instance = ClientLegalEntitySearch.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[InvoiceSearch] = None
        try:
            instance.actual_instance = InvoiceSearch.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[CommercialOfferSearch] = None
        try:
            instance.actual_instance = CommercialOfferSearch.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[ServiceContractSearch] = None
        try:
            instance.actual_instance = ServiceContractSearch.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Search200ResponseInner with anyOf schemas: ClientLegalEntitySearch, CommercialOfferSearch, InvoiceSearch, ServiceContractSearch. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ClientLegalEntitySearch, CommercialOfferSearch, InvoiceSearch, ServiceContractSearch]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


