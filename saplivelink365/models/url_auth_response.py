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


class UrlAuthResponse(object):
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
        'id': 'int',
        'message': 'str',
        'order_id': 'str',
        'status': 'str',
        'token': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'order_id': 'orderID',
        'status': 'status',
        'token': 'token'
    }

    def __init__(self, id=None, message=None, order_id=None, status=None, token=None, local_vars_configuration=None):  # noqa: E501
        """UrlAuthResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._message = None
        self._order_id = None
        self._status = None
        self._token = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if token is not None:
            self.token = token

    @property
    def id(self):
        """Gets the id of this UrlAuthResponse.  # noqa: E501

        Unique identifier for the URL authorization.  # noqa: E501

        :return: The id of this UrlAuthResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UrlAuthResponse.

        Unique identifier for the URL authorization.  # noqa: E501

        :param id: The id of this UrlAuthResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this UrlAuthResponse.  # noqa: E501

        Describes any errors that occurred.  # noqa: E501

        :return: The message of this UrlAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UrlAuthResponse.

        Describes any errors that occurred.  # noqa: E501

        :param message: The message of this UrlAuthResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def order_id(self):
        """Gets the order_id of this UrlAuthResponse.  # noqa: E501

        Unique ID that identifies the specific order corresponding to the URL authorization request.  # noqa: E501

        :return: The order_id of this UrlAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this UrlAuthResponse.

        Unique ID that identifies the specific order corresponding to the URL authorization request.  # noqa: E501

        :param order_id: The order_id of this UrlAuthResponse.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def status(self):
        """Gets the status of this UrlAuthResponse.  # noqa: E501

        Describes the success or failure of the URL authorization.  # noqa: E501

        :return: The status of this UrlAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UrlAuthResponse.

        Describes the success or failure of the URL authorization.  # noqa: E501

        :param status: The status of this UrlAuthResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def token(self):
        """Gets the token of this UrlAuthResponse.  # noqa: E501

        The authorization token that was generated from the request.  # noqa: E501

        :return: The token of this UrlAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UrlAuthResponse.

        The authorization token that was generated from the request.  # noqa: E501

        :param token: The token of this UrlAuthResponse.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if not isinstance(other, UrlAuthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UrlAuthResponse):
            return True

        return self.to_dict() != other.to_dict()