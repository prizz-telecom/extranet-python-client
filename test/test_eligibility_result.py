# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.eligibility_result import EligibilityResult

class TestEligibilityResult(unittest.TestCase):
    """EligibilityResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EligibilityResult:
        """Test EligibilityResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EligibilityResult`
        """
        model = EligibilityResult()
        if include_optional:
            return EligibilityResult(
                code = '',
                tech = 56,
                delivery = 56,
                grt_min = 56,
                grt_max = 56,
                grt_non_working_hours_option_available = True,
                grt_non_working_hours_option_mandatory = True,
                nrc_min = 56,
                nrc_max = 56,
                commitment_min = 56,
                commitment_max = 56,
                upload_min = 56,
                upload_max = 56,
                download_min = 56,
                download_max = 56,
                guaranteed_upload_min = 56,
                guaranteed_upload_max = 56,
                guaranteedd_download_min = 56,
                guaranteedd_download_max = 56,
                rc_min = 56,
                rc_max = 56,
                price_list_items_groups = prizz_extranet.models.eligibility_result_price_list_items_groups.EligibilityResult_priceListItemsGroups(
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
                            product_name = '', )
                        ], 
                    commitment = [
                        
                        ], 
                    grt = [
                        
                        ], 
                    nrc = [
                        
                        ], 
                    distance = [
                        
                        ], 
                    fiber_count = [
                        
                        ], 
                    extremity_site_a = [
                        
                        ], 
                    extremity_site_b = [
                        
                        ], 
                    maintenance = [
                        
                        ], 
                    subnet = [
                        
                        ], 
                    national = [
                        
                        ], ),
                offer_id = 56,
                price_list_id = 56,
                combinations = [
                    prizz_extranet.models.eligibility_result_combination.EligibilityResultCombination(
                        combination_id = '', 
                        total = 56, 
                        total_without_nrc = 56, 
                        nrc = 56, 
                        attributes = { }, )
                    ]
            )
        else:
            return EligibilityResult(
        )
        """

    def testEligibilityResult(self):
        """Test EligibilityResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
