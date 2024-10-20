# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.offer import Offer

class TestOffer(unittest.TestCase):
    """Offer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Offer:
        """Test Offer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Offer`
        """
        model = Offer()
        if include_optional:
            return Offer(
                id = 56,
                name = '',
                main_offer_item = prizz_extranet.models.offer_item.OfferItem(
                    id = 56, 
                    name = '', 
                    create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    min_count = 56, 
                    max_count = 56, 
                    product = prizz_extranet.models.product.Product(
                        id = 56, 
                        name = '', 
                        attributes = prizz_extranet.models.attributes.attributes(), 
                        product_code = '', 
                        group = prizz_extranet.models.product_group.ProductGroup(
                            name = '', 
                            type = 'bandwidth', ), ), 
                    eligibility_string = '', ),
                offer_type = 'DELIVERY_DOOR'
            )
        else:
            return Offer(
        )
        """

    def testOffer(self):
        """Test Offer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()