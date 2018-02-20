#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import sys
from collections import defaultdict

import pyhttpstatus_utils

if (sys.version_info[0] < 3) or (sys.version_info[0] == 3 and sys.version_info[2] < 5):
    from pyhttpstatus_utils import HTTPStatus
else:
    from http import HTTPStatus

class TestHttpStatus():

    def test_create_http_status_dict(self):
        msg_unexpected_status = 'Partner returned non-200 status code'

        _http_status_dict = defaultdict(
            lambda: msg_unexpected_status, pyhttpstatus_utils.create_http_status_dict({
                401: 'Invalid api_key'
            })
        )

        assert(_http_status_dict[200] == 'OK')
        assert(_http_status_dict[502] == 'Bad Gateway')
        assert(_http_status_dict[401] == 'Unauthorized: Invalid api_key.')
        assert(_http_status_dict[600] == msg_unexpected_status)

    def test_http_status_type(self):
        for http_status_code in pyhttpstatus_utils.HTTP_STATUS_TYPE_DICT:
            assert(type(http_status_code) is int)
            http_status_type = pyhttpstatus_utils.HTTP_STATUS_TYPE_DICT[http_status_code]
            assert(type(http_status_type) is str)

    def test_http_status_dict(self):
        for key in pyhttpstatus_utils.HTTP_STATUS_DICT:
            assert(type(key) is int)
            assert(type(pyhttpstatus_utils.HTTP_STATUS_DICT[key]) is dict)
            for field in pyhttpstatus_utils.HTTP_STATUS_DICT[key]:
                assert(type(field) is str)

    def test_http_status_phrase(self):
        for key in pyhttpstatus_utils.HTTP_STATUS_PHRASE_DICT:
            assert(type(key) is int)
            assert(type(pyhttpstatus_utils.HTTP_STATUS_PHRASE_DICT[key]) is str)

    def test_http_status(self):
        for httpstatus in list(HTTPStatus):
            assert(type(int(httpstatus)) is int)
            assert(type(httpstatus.name) is str)
            assert(type(httpstatus.phrase) is str)
            assert(type(httpstatus.description) is str)

    def test_is_http_status_successful(self):
        assert(pyhttpstatus_utils.is_http_status_successful(200))

    def test_http_status_code_to_type(self):
        __all_http_status_codes__ = list(map(int, HTTPStatus))

        for http_status_code in __all_http_status_codes__:
            assert(pyhttpstatus_utils.get_http_status_type(http_status_code))
            assert(type(pyhttpstatus_utils.is_http_status_successful(http_status_code)) is bool)

            if pyhttpstatus_utils.is_http_status_successful(http_status_code):
                assert(pyhttpstatus_utils.get_http_status_type(
                    http_status_code) == pyhttpstatus_utils.HttpStatusType.SUCCESSFUL)
            else:
                assert(pyhttpstatus_utils.get_http_status_type(
                    http_status_code) != pyhttpstatus_utils.HttpStatusType.SUCCESSFUL)

    def test_is_http_status_type(self):
        __all_http_status_codes__ = list(map(int, HTTPStatus))
        for http_status_code in __all_http_status_codes__:
            http_status_type = pyhttpstatus_utils.get_http_status_type(http_status_code)
            if pyhttpstatus_utils.is_http_status_successful(http_status_code):
                assert(http_status_type == pyhttpstatus_utils.HttpStatusType.SUCCESSFUL)
            else:
                assert(http_status_type != pyhttpstatus_utils.HttpStatusType.SUCCESSFUL)

            assert(pyhttpstatus_utils.is_http_status_type(http_status_code, http_status_type))

    def test_http_status_codes_list(self):
        _http_status_codes_list = [
            pyhttpstatus_utils.HttpStatusCode.BAD_GATEWAY,
            pyhttpstatus_utils.HttpStatusCode.SERVICE_UNAVAILABLE,
            pyhttpstatus_utils.HttpStatusCode.GATEWAY_TIMEOUT,
            pyhttpstatus_utils.HttpStatusCode.TOO_MANY_REQUESTS
        ]
        http_status_codes_list = list(map(int, _http_status_codes_list))

        assert(type(http_status_codes_list) is list)
        for http_status_code in http_status_codes_list:
            assert(type(http_status_code) is int)