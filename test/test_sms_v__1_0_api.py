# coding: utf-8

"""
    SAP Digital Interconnect LiveLink 365

    The SAP Live Link 365 is a communication platform as a service (CPaaS) that leverages robust delivery technology, SAP’s global relationships, and the power of SAP’s Cloud Platform to provide affordable, scalable, and global messaging solutions for best in class SMS management.  # noqa: E501

    The version of the OpenAPI document: v1.1.0
    Contact: sapdigitalinterconnect@sap.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import saplivelink365
from saplivelink365.api.sms_v__1_0_api import SMSV10Api  # noqa: E501
from saplivelink365.rest import ApiException


class TestSMSV10Api(unittest.TestCase):
    """SMSV10Api unit test stubs"""

    def setUp(self):
        self.api = saplivelink365.api.sms_v__1_0_api.SMSV10Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_receive_sms_using_post2(self):
        """Test case for receive_sms_using_post2

        Send SMS message  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
