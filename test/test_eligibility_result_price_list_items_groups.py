# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.eligibility_result_price_list_items_groups import EligibilityResultPriceListItemsGroups

class TestEligibilityResultPriceListItemsGroups(unittest.TestCase):
    """EligibilityResultPriceListItemsGroups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EligibilityResultPriceListItemsGroups:
        """Test EligibilityResultPriceListItemsGroups
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EligibilityResultPriceListItemsGroups`
        """
        model = EligibilityResultPriceListItemsGroups()
        if include_optional:
            return EligibilityResultPriceListItemsGroups(
                main = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                bandwidth = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                commitment = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                grt = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                nrc = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                distance = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                fiber_count = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                extremity_site_a = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                extremity_site_b = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                maintenance = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                subnet = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ],
                national = [
                    prizz_extranet.models.eligibility_price_list_item.EligibilityPriceListItem(
                        id = 56, 
                        name = '', 
                        product_name = '', 
                        attributes = { }, )
                    ]
            )
        else:
            return EligibilityResultPriceListItemsGroups(
        )
        """

    def testEligibilityResultPriceListItemsGroups(self):
        """Test EligibilityResultPriceListItemsGroups"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()