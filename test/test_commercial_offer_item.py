# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.commercial_offer_item import CommercialOfferItem

class TestCommercialOfferItem(unittest.TestCase):
    """CommercialOfferItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommercialOfferItem:
        """Test CommercialOfferItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommercialOfferItem`
        """
        model = CommercialOfferItem()
        if include_optional:
            return CommercialOfferItem(
                available_workflows = [
                    'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context'
                    ],
                id = 56,
                name = '',
                unit_price = 56,
                unit_price_str = '',
                unit = '',
                vat = '',
                recurrence = 'monthly',
                unit_price_discount = 56,
                unit_price_discount_str = '',
                quantity = 56,
                house_number = 56,
                house_number_complement = '',
                street_name = '',
                postal_code = '',
                city_name = '',
                insee_code = '',
                latitude = 1.337,
                longitude = 1.337,
                x = 1.337,
                y = 1.337,
                projection = '',
                price = 56,
                section_id = 56,
                commercial_offer_id = 56,
                price_str = '',
                vat_rate = 1.337,
                commercial_code = '',
                description = '',
                to_estimate = True,
                price_list_item = prizz_extranet.models.price_list_item.PriceListItem(
                    id = 56, 
                    create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    unit_price = 56, 
                    unit_price_str = '', 
                    unit = '', 
                    vat = '', 
                    recurrence = 'monthly', 
                    price_list_id = 56, 
                    product = prizz_extranet.models.product.Product(
                        id = 56, 
                        name = '', 
                        attributes = prizz_extranet.models.attributes.attributes(), 
                        product_code = '', 
                        group = prizz_extranet.models.product_group.ProductGroup(
                            name = '', 
                            type = 'bandwidth', ), ), 
                    commercial_code = '', 
                    description = '', 
                    inside_offer_only = True, 
                    to_estimate = True, 
                    active = True, )
            )
        else:
            return CommercialOfferItem(
        )
        """

    def testCommercialOfferItem(self):
        """Test CommercialOfferItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
