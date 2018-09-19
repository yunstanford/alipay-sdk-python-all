#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicMessageLabelSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicMessageLabelSendResponse, self).__init__()
        self._code = None
        self._msg = None
        self._msg_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicMessageLabelSendResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'msg' in response:
            self.msg = response['msg']
        if 'msg_id' in response:
            self.msg_id = response['msg_id']
