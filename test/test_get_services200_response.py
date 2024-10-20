# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.get_services200_response import GetServices200Response

class TestGetServices200Response(unittest.TestCase):
    """GetServices200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetServices200Response:
        """Test GetServices200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetServices200Response`
        """
        model = GetServices200Response()
        if include_optional:
            return GetServices200Response(
                pagination = prizz_extranet.models.get_client_legal_entities_200_response_pagination.getClientLegalEntities_200_response_pagination(
                    page = 56, 
                    items_per_page = 56, 
                    total_items = 56, 
                    page_count = 56, ),
                items = [
                    prizz_extranet.models.service.Service(
                        id = 56, 
                        name = '', 
                        unit_price_discount = 56, 
                        unit_price_discount_str = '', 
                        house_number = 56, 
                        house_number_complement = '', 
                        street_name = '', 
                        postal_code = '', 
                        city_name = '', 
                        insee_code = '', 
                        create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        attributes = prizz_extranet.models.attributes.attributes(), 
                        quantity = 56, 
                        unit_price = 56, 
                        unit_price_str = '', 
                        unit = '', 
                        vat = '', 
                        recurrence = 'monthly', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        x = 1.337, 
                        y = 1.337, 
                        projection = '', 
                        product = prizz_extranet.models.product.Product(
                            id = 56, 
                            name = '', 
                            attributes = prizz_extranet.models.attributes.attributes(), 
                            product_code = '', 
                            group = prizz_extranet.models.product_group.ProductGroup(
                                name = '', 
                                type = 'bandwidth', ), ), 
                        status = 'new', 
                        subscription_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        activation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        termination_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        service_contract_id = 56, 
                        paid_until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetServices200Response(
        )
        """

    def testGetServices200Response(self):
        """Test GetServices200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()