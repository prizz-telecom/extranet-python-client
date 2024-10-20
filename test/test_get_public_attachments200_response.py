# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.get_public_attachments200_response import GetPublicAttachments200Response

class TestGetPublicAttachments200Response(unittest.TestCase):
    """GetPublicAttachments200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPublicAttachments200Response:
        """Test GetPublicAttachments200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPublicAttachments200Response`
        """
        model = GetPublicAttachments200Response()
        if include_optional:
            return GetPublicAttachments200Response(
                attachments = [
                    prizz_extranet.models.attachment.Attachment(
                        id = 56, 
                        name = '', 
                        create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        category = '', 
                        mime_type = '', 
                        presigned_url = '', 
                        presigned_url_expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetPublicAttachments200Response(
        )
        """

    def testGetPublicAttachments200Response(self):
        """Test GetPublicAttachments200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
