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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from prizz_extranet.models.eligibility_price_list_item import EligibilityPriceListItem
from typing import Optional, Set
from typing_extensions import Self

class EligibilityResultPriceListItemsGroups(BaseModel):
    """
    Price list items grouped by product group
    """ # noqa: E501
    main: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Main product group, contains on item with base price")
    bandwidth: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Bandwidth product group, list available bandwidths")
    commitment: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Commitment product group, list available commitments")
    grt: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="GRT product group, list available GRT options")
    nrc: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="NRC product group, contain one item in most cases")
    distance: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Used in FON offers")
    fiber_count: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Used in FON offers")
    extremity_site_a: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Used in FON offers, describes the extremity A")
    extremity_site_b: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Used in FON offers, describes the extremity B")
    maintenance: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Used in FON offers")
    subnet: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Used in L3 offers, list available subnets sizes")
    national: Optional[List[EligibilityPriceListItem]] = Field(default=None, description="Used in L2 offers, list available national options")
    __properties: ClassVar[List[str]] = ["main", "bandwidth", "commitment", "grt", "nrc", "distance", "fiber_count", "extremity_site_a", "extremity_site_b", "maintenance", "subnet", "national"]

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
        """Create an instance of EligibilityResultPriceListItemsGroups from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in main (list)
        _items = []
        if self.main:
            for _item_main in self.main:
                if _item_main:
                    _items.append(_item_main.to_dict())
            _dict['main'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bandwidth (list)
        _items = []
        if self.bandwidth:
            for _item_bandwidth in self.bandwidth:
                if _item_bandwidth:
                    _items.append(_item_bandwidth.to_dict())
            _dict['bandwidth'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in commitment (list)
        _items = []
        if self.commitment:
            for _item_commitment in self.commitment:
                if _item_commitment:
                    _items.append(_item_commitment.to_dict())
            _dict['commitment'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in grt (list)
        _items = []
        if self.grt:
            for _item_grt in self.grt:
                if _item_grt:
                    _items.append(_item_grt.to_dict())
            _dict['grt'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nrc (list)
        _items = []
        if self.nrc:
            for _item_nrc in self.nrc:
                if _item_nrc:
                    _items.append(_item_nrc.to_dict())
            _dict['nrc'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in distance (list)
        _items = []
        if self.distance:
            for _item_distance in self.distance:
                if _item_distance:
                    _items.append(_item_distance.to_dict())
            _dict['distance'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fiber_count (list)
        _items = []
        if self.fiber_count:
            for _item_fiber_count in self.fiber_count:
                if _item_fiber_count:
                    _items.append(_item_fiber_count.to_dict())
            _dict['fiber_count'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in extremity_site_a (list)
        _items = []
        if self.extremity_site_a:
            for _item_extremity_site_a in self.extremity_site_a:
                if _item_extremity_site_a:
                    _items.append(_item_extremity_site_a.to_dict())
            _dict['extremity_site_a'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in extremity_site_b (list)
        _items = []
        if self.extremity_site_b:
            for _item_extremity_site_b in self.extremity_site_b:
                if _item_extremity_site_b:
                    _items.append(_item_extremity_site_b.to_dict())
            _dict['extremity_site_b'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in maintenance (list)
        _items = []
        if self.maintenance:
            for _item_maintenance in self.maintenance:
                if _item_maintenance:
                    _items.append(_item_maintenance.to_dict())
            _dict['maintenance'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subnet (list)
        _items = []
        if self.subnet:
            for _item_subnet in self.subnet:
                if _item_subnet:
                    _items.append(_item_subnet.to_dict())
            _dict['subnet'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in national (list)
        _items = []
        if self.national:
            for _item_national in self.national:
                if _item_national:
                    _items.append(_item_national.to_dict())
            _dict['national'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EligibilityResultPriceListItemsGroups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "main": [EligibilityPriceListItem.from_dict(_item) for _item in obj["main"]] if obj.get("main") is not None else None,
            "bandwidth": [EligibilityPriceListItem.from_dict(_item) for _item in obj["bandwidth"]] if obj.get("bandwidth") is not None else None,
            "commitment": [EligibilityPriceListItem.from_dict(_item) for _item in obj["commitment"]] if obj.get("commitment") is not None else None,
            "grt": [EligibilityPriceListItem.from_dict(_item) for _item in obj["grt"]] if obj.get("grt") is not None else None,
            "nrc": [EligibilityPriceListItem.from_dict(_item) for _item in obj["nrc"]] if obj.get("nrc") is not None else None,
            "distance": [EligibilityPriceListItem.from_dict(_item) for _item in obj["distance"]] if obj.get("distance") is not None else None,
            "fiber_count": [EligibilityPriceListItem.from_dict(_item) for _item in obj["fiber_count"]] if obj.get("fiber_count") is not None else None,
            "extremity_site_a": [EligibilityPriceListItem.from_dict(_item) for _item in obj["extremity_site_a"]] if obj.get("extremity_site_a") is not None else None,
            "extremity_site_b": [EligibilityPriceListItem.from_dict(_item) for _item in obj["extremity_site_b"]] if obj.get("extremity_site_b") is not None else None,
            "maintenance": [EligibilityPriceListItem.from_dict(_item) for _item in obj["maintenance"]] if obj.get("maintenance") is not None else None,
            "subnet": [EligibilityPriceListItem.from_dict(_item) for _item in obj["subnet"]] if obj.get("subnet") is not None else None,
            "national": [EligibilityPriceListItem.from_dict(_item) for _item in obj["national"]] if obj.get("national") is not None else None
        })
        return _obj


