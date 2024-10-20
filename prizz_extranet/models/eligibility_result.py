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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from prizz_extranet.models.eligibility_result_combination import EligibilityResultCombination
from prizz_extranet.models.eligibility_result_price_list_items_groups import EligibilityResultPriceListItemsGroups
from typing import Optional, Set
from typing_extensions import Self

class EligibilityResult(BaseModel):
    """
    EligibilityResult
    """ # noqa: E501
    code: Optional[StrictStr] = None
    tech: Optional[StrictInt] = None
    delivery: Optional[StrictInt] = None
    grt_min: Optional[StrictInt] = Field(default=None, alias="grtMin")
    grt_max: Optional[StrictInt] = Field(default=None, alias="grtMax")
    grt_non_working_hours_option_available: Optional[StrictBool] = Field(default=None, alias="grtNonWorkingHoursOptionAvailable")
    grt_non_working_hours_option_mandatory: Optional[StrictBool] = Field(default=None, alias="grtNonWorkingHoursOptionMandatory")
    nrc_min: Optional[StrictInt] = Field(default=None, alias="nrcMin")
    nrc_max: Optional[StrictInt] = Field(default=None, alias="nrcMax")
    commitment_min: Optional[StrictInt] = Field(default=None, alias="commitmentMin")
    commitment_max: Optional[StrictInt] = Field(default=None, alias="commitmentMax")
    upload_min: Optional[StrictInt] = Field(default=None, alias="uploadMin")
    upload_max: Optional[StrictInt] = Field(default=None, alias="uploadMax")
    download_min: Optional[StrictInt] = Field(default=None, alias="downloadMin")
    download_max: Optional[StrictInt] = Field(default=None, alias="downloadMax")
    guaranteed_upload_min: Optional[StrictInt] = Field(default=None, alias="guaranteedUploadMin")
    guaranteed_upload_max: Optional[StrictInt] = Field(default=None, alias="guaranteedUploadMax")
    guaranteedd_download_min: Optional[StrictInt] = Field(default=None, alias="guaranteeddDownloadMin")
    guaranteedd_download_max: Optional[StrictInt] = Field(default=None, alias="guaranteeddDownloadMax")
    rc_min: Optional[StrictInt] = Field(default=None, alias="rcMin")
    rc_max: Optional[StrictInt] = Field(default=None, alias="rcMax")
    price_list_items_groups: Optional[EligibilityResultPriceListItemsGroups] = Field(default=None, alias="priceListItemsGroups")
    offer_id: Optional[StrictInt] = Field(default=None, alias="offerId")
    price_list_id: Optional[StrictInt] = Field(default=None, alias="priceListId")
    combinations: Optional[List[EligibilityResultCombination]] = None
    __properties: ClassVar[List[str]] = ["code", "tech", "delivery", "grtMin", "grtMax", "grtNonWorkingHoursOptionAvailable", "grtNonWorkingHoursOptionMandatory", "nrcMin", "nrcMax", "commitmentMin", "commitmentMax", "uploadMin", "uploadMax", "downloadMin", "downloadMax", "guaranteedUploadMin", "guaranteedUploadMax", "guaranteeddDownloadMin", "guaranteeddDownloadMax", "rcMin", "rcMax", "priceListItemsGroups", "offerId", "priceListId", "combinations"]

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
        """Create an instance of EligibilityResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price_list_items_groups
        if self.price_list_items_groups:
            _dict['priceListItemsGroups'] = self.price_list_items_groups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in combinations (list)
        _items = []
        if self.combinations:
            for _item_combinations in self.combinations:
                if _item_combinations:
                    _items.append(_item_combinations.to_dict())
            _dict['combinations'] = _items
        # set to None if delivery (nullable) is None
        # and model_fields_set contains the field
        if self.delivery is None and "delivery" in self.model_fields_set:
            _dict['delivery'] = None

        # set to None if grt_min (nullable) is None
        # and model_fields_set contains the field
        if self.grt_min is None and "grt_min" in self.model_fields_set:
            _dict['grtMin'] = None

        # set to None if grt_max (nullable) is None
        # and model_fields_set contains the field
        if self.grt_max is None and "grt_max" in self.model_fields_set:
            _dict['grtMax'] = None

        # set to None if nrc_min (nullable) is None
        # and model_fields_set contains the field
        if self.nrc_min is None and "nrc_min" in self.model_fields_set:
            _dict['nrcMin'] = None

        # set to None if nrc_max (nullable) is None
        # and model_fields_set contains the field
        if self.nrc_max is None and "nrc_max" in self.model_fields_set:
            _dict['nrcMax'] = None

        # set to None if commitment_min (nullable) is None
        # and model_fields_set contains the field
        if self.commitment_min is None and "commitment_min" in self.model_fields_set:
            _dict['commitmentMin'] = None

        # set to None if commitment_max (nullable) is None
        # and model_fields_set contains the field
        if self.commitment_max is None and "commitment_max" in self.model_fields_set:
            _dict['commitmentMax'] = None

        # set to None if upload_min (nullable) is None
        # and model_fields_set contains the field
        if self.upload_min is None and "upload_min" in self.model_fields_set:
            _dict['uploadMin'] = None

        # set to None if upload_max (nullable) is None
        # and model_fields_set contains the field
        if self.upload_max is None and "upload_max" in self.model_fields_set:
            _dict['uploadMax'] = None

        # set to None if download_min (nullable) is None
        # and model_fields_set contains the field
        if self.download_min is None and "download_min" in self.model_fields_set:
            _dict['downloadMin'] = None

        # set to None if download_max (nullable) is None
        # and model_fields_set contains the field
        if self.download_max is None and "download_max" in self.model_fields_set:
            _dict['downloadMax'] = None

        # set to None if guaranteed_upload_min (nullable) is None
        # and model_fields_set contains the field
        if self.guaranteed_upload_min is None and "guaranteed_upload_min" in self.model_fields_set:
            _dict['guaranteedUploadMin'] = None

        # set to None if guaranteed_upload_max (nullable) is None
        # and model_fields_set contains the field
        if self.guaranteed_upload_max is None and "guaranteed_upload_max" in self.model_fields_set:
            _dict['guaranteedUploadMax'] = None

        # set to None if guaranteedd_download_min (nullable) is None
        # and model_fields_set contains the field
        if self.guaranteedd_download_min is None and "guaranteedd_download_min" in self.model_fields_set:
            _dict['guaranteeddDownloadMin'] = None

        # set to None if guaranteedd_download_max (nullable) is None
        # and model_fields_set contains the field
        if self.guaranteedd_download_max is None and "guaranteedd_download_max" in self.model_fields_set:
            _dict['guaranteeddDownloadMax'] = None

        # set to None if rc_min (nullable) is None
        # and model_fields_set contains the field
        if self.rc_min is None and "rc_min" in self.model_fields_set:
            _dict['rcMin'] = None

        # set to None if rc_max (nullable) is None
        # and model_fields_set contains the field
        if self.rc_max is None and "rc_max" in self.model_fields_set:
            _dict['rcMax'] = None

        # set to None if offer_id (nullable) is None
        # and model_fields_set contains the field
        if self.offer_id is None and "offer_id" in self.model_fields_set:
            _dict['offerId'] = None

        # set to None if price_list_id (nullable) is None
        # and model_fields_set contains the field
        if self.price_list_id is None and "price_list_id" in self.model_fields_set:
            _dict['priceListId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EligibilityResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "tech": obj.get("tech"),
            "delivery": obj.get("delivery"),
            "grtMin": obj.get("grtMin"),
            "grtMax": obj.get("grtMax"),
            "grtNonWorkingHoursOptionAvailable": obj.get("grtNonWorkingHoursOptionAvailable"),
            "grtNonWorkingHoursOptionMandatory": obj.get("grtNonWorkingHoursOptionMandatory"),
            "nrcMin": obj.get("nrcMin"),
            "nrcMax": obj.get("nrcMax"),
            "commitmentMin": obj.get("commitmentMin"),
            "commitmentMax": obj.get("commitmentMax"),
            "uploadMin": obj.get("uploadMin"),
            "uploadMax": obj.get("uploadMax"),
            "downloadMin": obj.get("downloadMin"),
            "downloadMax": obj.get("downloadMax"),
            "guaranteedUploadMin": obj.get("guaranteedUploadMin"),
            "guaranteedUploadMax": obj.get("guaranteedUploadMax"),
            "guaranteeddDownloadMin": obj.get("guaranteeddDownloadMin"),
            "guaranteeddDownloadMax": obj.get("guaranteeddDownloadMax"),
            "rcMin": obj.get("rcMin"),
            "rcMax": obj.get("rcMax"),
            "priceListItemsGroups": EligibilityResultPriceListItemsGroups.from_dict(obj["priceListItemsGroups"]) if obj.get("priceListItemsGroups") is not None else None,
            "offerId": obj.get("offerId"),
            "priceListId": obj.get("priceListId"),
            "combinations": [EligibilityResultCombination.from_dict(_item) for _item in obj["combinations"]] if obj.get("combinations") is not None else None
        })
        return _obj

