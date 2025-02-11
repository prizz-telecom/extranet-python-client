# coding: utf-8

"""
    Prizz-Telecom Extranet API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from prizz_extranet.models.transition_form_fields_inner import TransitionFormFieldsInner

class TestTransitionFormFieldsInner(unittest.TestCase):
    """TransitionFormFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransitionFormFieldsInner:
        """Test TransitionFormFieldsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransitionFormFieldsInner`
        """
        model = TransitionFormFieldsInner()
        if include_optional:
            return TransitionFormFieldsInner(
                caption = '',
                name = '',
                required = True,
                value = '',
                values = [
                    prizz_extranet.models.transition_form_fields_inner_values_inner.Transition_formFields_inner_values_inner(
                        key = '', 
                        value = '', )
                    ],
                type = '',
                help = '',
                multiple = True,
                expanded = True
            )
        else:
            return TransitionFormFieldsInner(
        )
        """

    def testTransitionFormFieldsInner(self):
        """Test TransitionFormFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
