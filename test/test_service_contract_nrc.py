# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.service_contract_nrc import ServiceContractNrc

class TestServiceContractNrc(unittest.TestCase):
    """ServiceContractNrc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceContractNrc:
        """Test ServiceContractNrc
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceContractNrc`
        """
        model = ServiceContractNrc()
        if include_optional:
            return ServiceContractNrc(
                id = 56,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                unit_price = 56,
                unit_price_str = '',
                unit = '',
                vat = '',
                recurrence = 'monthly',
                quantity = 56,
                unit_price_discount = 56,
                unit_price_discount_str = '',
                attributes = prizz_extranet.models.attributes.attributes(),
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
                service_contract_id = 56,
                base_item_id = 56,
                billed = True,
                price = 56,
                price_str = '',
                va_trate = 1.337,
                commercial_code = '',
                description = '',
                type = ''
            )
        else:
            return ServiceContractNrc(
        )
        """

    def testServiceContractNrc(self):
        """Test ServiceContractNrc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()