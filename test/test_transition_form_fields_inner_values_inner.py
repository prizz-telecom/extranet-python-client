# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.transition_form_fields_inner_values_inner import TransitionFormFieldsInnerValuesInner

class TestTransitionFormFieldsInnerValuesInner(unittest.TestCase):
    """TransitionFormFieldsInnerValuesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransitionFormFieldsInnerValuesInner:
        """Test TransitionFormFieldsInnerValuesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransitionFormFieldsInnerValuesInner`
        """
        model = TransitionFormFieldsInnerValuesInner()
        if include_optional:
            return TransitionFormFieldsInnerValuesInner(
                key = '',
                value = ''
            )
        else:
            return TransitionFormFieldsInnerValuesInner(
        )
        """

    def testTransitionFormFieldsInnerValuesInner(self):
        """Test TransitionFormFieldsInnerValuesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
