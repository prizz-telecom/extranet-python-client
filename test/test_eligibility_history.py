# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.eligibility_history import EligibilityHistory

class TestEligibilityHistory(unittest.TestCase):
    """EligibilityHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EligibilityHistory:
        """Test EligibilityHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EligibilityHistory`
        """
        model = EligibilityHistory()
        if include_optional:
            return EligibilityHistory(
                id = 56,
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                address = '',
                client = prizz_extranet.models.client_legal_entity.ClientLegalEntity(
                    available_workflows = [
                        'Infracorp\\Services\\Workflow\\ClientLegalEntity\\CreateCommercialOffer\\Context'
                        ], 
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
                    arcep_code = '', 
                    contacts = [
                        prizz_extranet.models.contact.Contact(
                            id = 56, 
                            firstname = '', 
                            lastname = '', 
                            company_name = '', 
                            email = '', 
                            phone1 = '', 
                            phone2 = '', 
                            gender = '', 
                            create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    configured_contacts = [
                        prizz_extranet.models.typed_contact.TypedContact(
                            id = 56, 
                            create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            entity_id = 56, 
                            entity_class = '', 
                            contact = prizz_extranet.models.contact.Contact(
                                id = 56, 
                                firstname = '', 
                                lastname = '', 
                                company_name = '', 
                                email = '', 
                                phone1 = '', 
                                phone2 = '', 
                                gender = '', 
                                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            type = 'DELIVERY', )
                        ], 
                    contracts = [
                        prizz_extranet.models.client_contract.ClientContract(
                            id = 56, 
                            name = '', 
                            price_list = prizz_extranet.models.price_list.PriceList(
                                id = 56, 
                                name = '', 
                                legal_entity = prizz_extranet.models.legal_entity.LegalEntity(
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
                                    logo = '', ), 
                                commercial_code = '', 
                                description = '', 
                                items = [
                                    prizz_extranet.models.price_list_item.PriceListItem(
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
                                    ], ), 
                            payment_term_days = 56, 
                            vat_reverse_charge = True, 
                            invoice_consolidation = True, )
                        ], 
                    roles = [
                        prizz_extranet.models.user_role.UserRole(
                            id = 56, 
                            create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user = prizz_extranet.models.user.User(
                                id = 56, 
                                firstname = '', 
                                lastname = '', 
                                company_name = '', 
                                email = '', 
                                phone1 = '', 
                                phone2 = '', 
                                gender = '', 
                                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            role = '', )
                        ], ),
                result = [
                    prizz_extranet.models.eligibility_result.EligibilityResult(
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
                                total_without_nrc = 56, )
                            ], )
                    ]
            )
        else:
            return EligibilityHistory(
        )
        """

    def testEligibilityHistory(self):
        """Test EligibilityHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
