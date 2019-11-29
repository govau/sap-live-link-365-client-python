# coding: utf-8

"""
    SAP Digital Interconnect LiveLink 365

    The SAP Live Link 365 is a communication platform as a service (CPaaS) that leverages robust delivery technology, SAP’s global relationships, and the power of SAP’s Cloud Platform to provide affordable, scalable, and global messaging solutions for best in class SMS management.  # noqa: E501

    The version of the OpenAPI document: v1.1.0
    Contact: sapdigitalinterconnect@sap.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from saplivelink365.configuration import Configuration


class UrlAuthorizationRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'account_id': 'int',
        'telephone_number': 'int',
        'email_address': 'int',
        'message_body': 'str',
        'character_set': 'str',
        'token_length': 'int',
        'pin_type': 'int',
        'time_out': 'int',
        'secondarykey': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'telephone_number': 'telephoneNumber',
        'email_address': 'emailAddress',
        'message_body': 'messageBody',
        'character_set': 'characterSet',
        'token_length': 'tokenLength',
        'pin_type': 'pinType',
        'time_out': 'timeOut',
        'secondarykey': 'secondarykey'
    }

    def __init__(self, account_id=None, telephone_number=None, email_address=None, message_body=None, character_set=None, token_length=None, pin_type=None, time_out=None, secondarykey=None, local_vars_configuration=None):  # noqa: E501
        """UrlAuthorizationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._telephone_number = None
        self._email_address = None
        self._message_body = None
        self._character_set = None
        self._token_length = None
        self._pin_type = None
        self._time_out = None
        self._secondarykey = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        self.telephone_number = telephone_number
        self.email_address = email_address
        if message_body is not None:
            self.message_body = message_body
        if character_set is not None:
            self.character_set = character_set
        if token_length is not None:
            self.token_length = token_length
        if pin_type is not None:
            self.pin_type = pin_type
        if time_out is not None:
            self.time_out = time_out
        if secondarykey is not None:
            self.secondarykey = secondarykey

    @property
    def account_id(self):
        """Gets the account_id of this UrlAuthorizationRequest.  # noqa: E501

        The System account that will have access to send messages through the HUB Account. This is the MFA account ID.  # noqa: E501

        :return: The account_id of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this UrlAuthorizationRequest.

        The System account that will have access to send messages through the HUB Account. This is the MFA account ID.  # noqa: E501

        :param account_id: The account_id of this UrlAuthorizationRequest.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def telephone_number(self):
        """Gets the telephone_number of this UrlAuthorizationRequest.  # noqa: E501

        The user phone number that will receive the token.  # noqa: E501

        :return: The telephone_number of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        """Sets the telephone_number of this UrlAuthorizationRequest.

        The user phone number that will receive the token.  # noqa: E501

        :param telephone_number: The telephone_number of this UrlAuthorizationRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and telephone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `telephone_number`, must not be `None`")  # noqa: E501

        self._telephone_number = telephone_number

    @property
    def email_address(self):
        """Gets the email_address of this UrlAuthorizationRequest.  # noqa: E501

        Email address that will receive the token.  # noqa: E501

        :return: The email_address of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UrlAuthorizationRequest.

        Email address that will receive the token.  # noqa: E501

        :param email_address: The email_address of this UrlAuthorizationRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def message_body(self):
        """Gets the message_body of this UrlAuthorizationRequest.  # noqa: E501

        The message that will be carried over with the token.  # noqa: E501

        :return: The message_body of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this UrlAuthorizationRequest.

        The message that will be carried over with the token.  # noqa: E501

        :param message_body: The message_body of this UrlAuthorizationRequest.  # noqa: E501
        :type: str
        """

        self._message_body = message_body

    @property
    def character_set(self):
        """Gets the character_set of this UrlAuthorizationRequest.  # noqa: E501

        It is the Message Character set.  # noqa: E501

        :return: The character_set of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this UrlAuthorizationRequest.

        It is the Message Character set.  # noqa: E501

        :param character_set: The character_set of this UrlAuthorizationRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["8b", "BIG5", "UTF8", "GB2312", "8859-7", "BIG5 and UCS2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and character_set not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `character_set` ({0}), must be one of {1}"  # noqa: E501
                .format(character_set, allowed_values)
            )

        self._character_set = character_set

    @property
    def token_length(self):
        """Gets the token_length of this UrlAuthorizationRequest.  # noqa: E501

        Number of characters the token will contain.  # noqa: E501

        :return: The token_length of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._token_length

    @token_length.setter
    def token_length(self, token_length):
        """Sets the token_length of this UrlAuthorizationRequest.

        Number of characters the token will contain.  # noqa: E501

        :param token_length: The token_length of this UrlAuthorizationRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                token_length is not None and token_length > 9):  # noqa: E501
            raise ValueError("Invalid value for `token_length`, must be a value less than or equal to `9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                token_length is not None and token_length < 4):  # noqa: E501
            raise ValueError("Invalid value for `token_length`, must be a value greater than or equal to `4`")  # noqa: E501

        self._token_length = token_length

    @property
    def pin_type(self):
        """Gets the pin_type of this UrlAuthorizationRequest.  # noqa: E501

        Type of PIN. 0 for Numeric and 1 for Alphanumeric.  # noqa: E501

        :return: The pin_type of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._pin_type

    @pin_type.setter
    def pin_type(self, pin_type):
        """Sets the pin_type of this UrlAuthorizationRequest.

        Type of PIN. 0 for Numeric and 1 for Alphanumeric.  # noqa: E501

        :param pin_type: The pin_type of this UrlAuthorizationRequest.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and pin_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `pin_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pin_type, allowed_values)
            )

        self._pin_type = pin_type

    @property
    def time_out(self):
        """Gets the time_out of this UrlAuthorizationRequest.  # noqa: E501

        Token's validity lifetime in seconds.  # noqa: E501

        :return: The time_out of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._time_out

    @time_out.setter
    def time_out(self, time_out):
        """Sets the time_out of this UrlAuthorizationRequest.

        Token's validity lifetime in seconds.  # noqa: E501

        :param time_out: The time_out of this UrlAuthorizationRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                time_out is not None and time_out > 900):  # noqa: E501
            raise ValueError("Invalid value for `time_out`, must be a value less than or equal to `900`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_out is not None and time_out < 30):  # noqa: E501
            raise ValueError("Invalid value for `time_out`, must be a value greater than or equal to `30`")  # noqa: E501

        self._time_out = time_out

    @property
    def secondarykey(self):
        """Gets the secondarykey of this UrlAuthorizationRequest.  # noqa: E501

        Secondary key which will be attached to the key while generating the token.  # noqa: E501

        :return: The secondarykey of this UrlAuthorizationRequest.  # noqa: E501
        :rtype: str
        """
        return self._secondarykey

    @secondarykey.setter
    def secondarykey(self, secondarykey):
        """Sets the secondarykey of this UrlAuthorizationRequest.

        Secondary key which will be attached to the key while generating the token.  # noqa: E501

        :param secondarykey: The secondarykey of this UrlAuthorizationRequest.  # noqa: E501
        :type: str
        """

        self._secondarykey = secondarykey

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UrlAuthorizationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UrlAuthorizationRequest):
            return True

        return self.to_dict() != other.to_dict()
