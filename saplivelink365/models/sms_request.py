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


class SmsRequest(object):
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
        'client_id': 'int',
        'body': 'str',
        'channel': 'str',
        'origin': 'str',
        'destination': 'list[str]',
        'ack_type': 'str',
        'validity_period': 'str',
        'session_id': 'str',
        'content_text_encoding': 'str',
        'subject': 'str',
        'mobile_notification': 'str',
        'operator_id': 'str',
        'message_class': 'str',
        'p_id': 'str',
        'ack_flags': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'body': 'body',
        'channel': 'channel',
        'origin': 'origin',
        'destination': 'destination',
        'ack_type': 'ackType',
        'validity_period': 'validityPeriod',
        'session_id': 'sessionId',
        'content_text_encoding': 'contentTextEncoding',
        'subject': 'subject',
        'mobile_notification': 'mobileNotification',
        'operator_id': 'operatorId',
        'message_class': 'messageClass',
        'p_id': 'pId',
        'ack_flags': 'ackFlags'
    }

    def __init__(self, client_id=None, body=None, channel='SMS', origin=None, destination=None, ack_type='ORDER', validity_period=None, session_id=None, content_text_encoding=None, subject=None, mobile_notification=None, operator_id=None, message_class=None, p_id=None, ack_flags=None, local_vars_configuration=None):  # noqa: E501
        """SmsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._body = None
        self._channel = None
        self._origin = None
        self._destination = None
        self._ack_type = None
        self._validity_period = None
        self._session_id = None
        self._content_text_encoding = None
        self._subject = None
        self._mobile_notification = None
        self._operator_id = None
        self._message_class = None
        self._p_id = None
        self._ack_flags = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        self.body = body
        if channel is not None:
            self.channel = channel
        if origin is not None:
            self.origin = origin
        self.destination = destination
        if ack_type is not None:
            self.ack_type = ack_type
        if validity_period is not None:
            self.validity_period = validity_period
        if session_id is not None:
            self.session_id = session_id
        if content_text_encoding is not None:
            self.content_text_encoding = content_text_encoding
        if subject is not None:
            self.subject = subject
        if mobile_notification is not None:
            self.mobile_notification = mobile_notification
        if operator_id is not None:
            self.operator_id = operator_id
        if message_class is not None:
            self.message_class = message_class
        if p_id is not None:
            self.p_id = p_id
        if ack_flags is not None:
            self.ack_flags = ack_flags

    @property
    def client_id(self):
        """Gets the client_id of this SmsRequest.  # noqa: E501

        Represents the client account.  # noqa: E501

        :return: The client_id of this SmsRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SmsRequest.

        Represents the client account.  # noqa: E501

        :param client_id: The client_id of this SmsRequest.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def body(self):
        """Gets the body of this SmsRequest.  # noqa: E501

        The Message body for the SMS.  # noqa: E501

        :return: The body of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SmsRequest.

        The Message body for the SMS.  # noqa: E501

        :param body: The body of this SmsRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def channel(self):
        """Gets the channel of this SmsRequest.  # noqa: E501

        Channel through which message will be delivered. This value should be: \"SMS\".  # noqa: E501

        :return: The channel of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this SmsRequest.

        Channel through which message will be delivered. This value should be: \"SMS\".  # noqa: E501

        :param channel: The channel of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def origin(self):
        """Gets the origin of this SmsRequest.  # noqa: E501

        Live Link number from which message will be sent.  # noqa: E501

        :return: The origin of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this SmsRequest.

        Live Link number from which message will be sent.  # noqa: E501

        :param origin: The origin of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def destination(self):
        """Gets the destination of this SmsRequest.  # noqa: E501

        An array of destination numbers that will receive the message.  # noqa: E501

        :return: The destination of this SmsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this SmsRequest.

        An array of destination numbers that will receive the message.  # noqa: E501

        :param destination: The destination of this SmsRequest.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and destination is None:  # noqa: E501
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def ack_type(self):
        """Gets the ack_type of this SmsRequest.  # noqa: E501

        Level of notification SAP will send back.  # noqa: E501

        :return: The ack_type of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._ack_type

    @ack_type.setter
    def ack_type(self, ack_type):
        """Sets the ack_type of this SmsRequest.

        Level of notification SAP will send back.  # noqa: E501

        :param ack_type: The ack_type of this SmsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ORDER", "MESSAGE", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ack_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ack_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ack_type, allowed_values)
            )

        self._ack_type = ack_type

    @property
    def validity_period(self):
        """Gets the validity_period of this SmsRequest.  # noqa: E501

        Time frame within which SAP will try to send the message. The time can be specified in weeks, days, hours or minutes.  # noqa: E501

        :return: The validity_period of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        """Sets the validity_period of this SmsRequest.

        Time frame within which SAP will try to send the message. The time can be specified in weeks, days, hours or minutes.  # noqa: E501

        :param validity_period: The validity_period of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._validity_period = validity_period

    @property
    def session_id(self):
        """Gets the session_id of this SmsRequest.  # noqa: E501

        It is needed for US campaign tracking.  # noqa: E501

        :return: The session_id of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this SmsRequest.

        It is needed for US campaign tracking.  # noqa: E501

        :param session_id: The session_id of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def content_text_encoding(self):
        """Gets the content_text_encoding of this SmsRequest.  # noqa: E501

        Specifies the message's text encoding.  # noqa: E501

        :return: The content_text_encoding of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_text_encoding

    @content_text_encoding.setter
    def content_text_encoding(self, content_text_encoding):
        """Sets the content_text_encoding of this SmsRequest.

        Specifies the message's text encoding.  # noqa: E501

        :param content_text_encoding: The content_text_encoding of this SmsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["8b", "BIG5", "UTF8", "GB2312", "8859-7", "UCS2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and content_text_encoding not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `content_text_encoding` ({0}), must be one of {1}"  # noqa: E501
                .format(content_text_encoding, allowed_values)
            )

        self._content_text_encoding = content_text_encoding

    @property
    def subject(self):
        """Gets the subject of this SmsRequest.  # noqa: E501

        Sets the message's subject. The subject will be returned in notifications and will ease tracking of message statuses.  # noqa: E501

        :return: The subject of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SmsRequest.

        Sets the message's subject. The subject will be returned in notifications and will ease tracking of message statuses.  # noqa: E501

        :param subject: The subject of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def mobile_notification(self):
        """Gets the mobile_notification of this SmsRequest.  # noqa: E501

        A Mobile Notification is an operator-dependent feature.  # noqa: E501

        :return: The mobile_notification of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_notification

    @mobile_notification.setter
    def mobile_notification(self, mobile_notification):
        """Sets the mobile_notification of this SmsRequest.

        A Mobile Notification is an operator-dependent feature.  # noqa: E501

        :param mobile_notification: The mobile_notification of this SmsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mobile_notification not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mobile_notification` ({0}), must be one of {1}"  # noqa: E501
                .format(mobile_notification, allowed_values)
            )

        self._mobile_notification = mobile_notification

    @property
    def operator_id(self):
        """Gets the operator_id of this SmsRequest.  # noqa: E501

        Used to specify the destination operators for the message.  # noqa: E501

        :return: The operator_id of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator_id

    @operator_id.setter
    def operator_id(self, operator_id):
        """Sets the operator_id of this SmsRequest.

        Used to specify the destination operators for the message.  # noqa: E501

        :param operator_id: The operator_id of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._operator_id = operator_id

    @property
    def message_class(self):
        """Gets the message_class of this SmsRequest.  # noqa: E501

        Used to specify the message class. Message class is an operator-dependent feature.  For example: 0 = Immediate display (flash) 1 = Handset Specific (LiveLink Default) 2 = SIM Specific 3 = TE Specific.  # noqa: E501

        :return: The message_class of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._message_class

    @message_class.setter
    def message_class(self, message_class):
        """Sets the message_class of this SmsRequest.

        Used to specify the message class. Message class is an operator-dependent feature.  For example: 0 = Immediate display (flash) 1 = Handset Specific (LiveLink Default) 2 = SIM Specific 3 = TE Specific.  # noqa: E501

        :param message_class: The message_class of this SmsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["0", "1", "2", "3"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and message_class not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `message_class` ({0}), must be one of {1}"  # noqa: E501
                .format(message_class, allowed_values)
            )

        self._message_class = message_class

    @property
    def p_id(self):
        """Gets the p_id of this SmsRequest.  # noqa: E501

         When a special value is needed, give the hexadecimal PID code you wish the request to carry.  # noqa: E501

        :return: The p_id of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._p_id

    @p_id.setter
    def p_id(self, p_id):
        """Sets the p_id of this SmsRequest.

         When a special value is needed, give the hexadecimal PID code you wish the request to carry.  # noqa: E501

        :param p_id: The p_id of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._p_id = p_id

    @property
    def ack_flags(self):
        """Gets the ack_flags of this SmsRequest.  # noqa: E501

        Represents various types of acknowledgements.  # noqa: E501

        :return: The ack_flags of this SmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._ack_flags

    @ack_flags.setter
    def ack_flags(self, ack_flags):
        """Sets the ack_flags of this SmsRequest.

        Represents various types of acknowledgements.  # noqa: E501

        :param ack_flags: The ack_flags of this SmsRequest.  # noqa: E501
        :type: str
        """

        self._ack_flags = ack_flags

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
        if not isinstance(other, SmsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmsRequest):
            return True

        return self.to_dict() != other.to_dict()
