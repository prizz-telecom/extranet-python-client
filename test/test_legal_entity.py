# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.legal_entity import LegalEntity

class TestLegalEntity(unittest.TestCase):
    """LegalEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegalEntity:
        """Test LegalEntity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegalEntity`
        """
        model = LegalEntity()
        if include_optional:
            return LegalEntity(
                id = 56,
                name = '',
                house_number = 56,
                house_number_complement = '',
                street_name = '',
                postal_code = '',
                city_name = '',
                insee_code = '',
                url = '',
                num_vat_intracommunity = '',
                siren = '',
                code_ape = '',
                rcs = '',
                tel = '',
                email = '',
                latitude = 1.337,
                longitude = 1.337,
                x = 1.337,
                y = 1.337,
                projection = '',
                logo = ''
            )
        else:
            return LegalEntity(
        )
        """

    def testLegalEntity(self):
        """Test LegalEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
