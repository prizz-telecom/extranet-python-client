# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.process_attributes import ProcessAttributes

class TestProcessAttributes(unittest.TestCase):
    """ProcessAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessAttributes:
        """Test ProcessAttributes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProcessAttributes`
        """
        model = ProcessAttributes()
        if include_optional:
            return ProcessAttributes(
                verif_cablage_ok = True,
                etat_voyants = '',
                qualification = prizz_extranet.models.process_attributes_qualification.ProcessAttributes_qualification(
                    values = prizz_extranet.models.process_attributes_qualification_values.ProcessAttributes_qualification_values(
                        type = '', 
                        description = '', 
                        date_debut_incident = '', ), ),
                customer_mails = [
                    ''
                    ],
                messages = prizz_extranet.models.process_attributes_messages.ProcessAttributes_messages(
                    operateur = [
                        prizz_extranet.models.process_message.ProcessMessage(
                            date = '', 
                            format = '', 
                            author = '', 
                            freeze = True, 
                            from_us = True, 
                            message = '', )
                        ], 
                    noc = [
                        prizz_extranet.models.process_message.ProcessMessage(
                            date = '', 
                            format = '', 
                            author = '', 
                            freeze = True, 
                            from_us = True, 
                            message = '', )
                        ], 
                    terrain = [
                        
                        ], )
            )
        else:
            return ProcessAttributes(
        )
        """

    def testProcessAttributes(self):
        """Test ProcessAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()