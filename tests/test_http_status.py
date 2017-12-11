#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

from collections import defaultdict
import http
import pyhttpstatus_utils

class TestHttpStatus():

    def test_status(self):
        msg_unexpected_status = 'Partner returned non-200 status code'

        _http_status_dict = defaultdict(
            lambda: msg_unexpected_status, pyhttpstatus_utils.http_status_dict({
                401: 'Invalid api_key'
            })
        )

        assert(_http_status_dict[200] == 'OK')
        assert(_http_status_dict[502] == 'Bad Gateway')
        assert(_http_status_dict[401] == 'Unauthorized: Invalid api_key.')
        assert(_http_status_dict[600] == msg_unexpected_status)

    def test_code_to_type(self):
        for http_status_code in pyhttpstatus_utils.HTTP_STATUS_CODE_TO_TYPE:
            assert(type(http_status_code) is int)
            status_type_obj = pyhttpstatus_utils.HTTP_STATUS_CODE_TO_TYPE[http_status_code]
            assert(type(status_type_obj) is pyhttpstatus_utils.HttpStatusType)
            assert(type(status_type_obj.name) is str)
            assert(type(status_type_obj.value) is str)

    def test_http_status_dict(self):
        for key in pyhttpstatus_utils.HTTP_STATUS_DICT:
            assert(type(key) is int)
            assert(type(pyhttpstatus_utils.HTTP_STATUS_DICT[key]) is dict)
            for field in pyhttpstatus_utils.HTTP_STATUS_DICT[key]:
                assert(type(field) is str)

    def test_http_status_code_to_phrase(self):
        for key in pyhttpstatus_utils.HTTP_STATUS_CODE_TO_PHRASE:
            assert(type(key) is int)
            assert(type(pyhttpstatus_utils.HTTP_STATUS_CODE_TO_PHRASE[key]) is str)

    def test_http_status_code(self):
        for httpstatus in list(http.HTTPStatus):
            assert(type(int(httpstatus)) is int)
            assert(type(httpstatus.name) is str)
            assert(type(httpstatus.phrase) is str)
            assert(type(httpstatus.description) is str)

    def test_is_http_status_successful(self):
        assert(pyhttpstatus_utils.is_http_status_successful(200))

    def test_http_status_code_to_type(self):
        _all_http_status_codes_ = list(map(int, pyhttpstatus_utils.HttpStatusCode))

        for http_status_code in _all_http_status_codes_:
            assert(pyhttpstatus_utils.http_status_code_to_type(http_status_code))
            assert(type(pyhttpstatus_utils.is_http_status_successful(http_status_code)) is bool)

            if pyhttpstatus_utils.is_http_status_successful(http_status_code):
                assert(pyhttpstatus_utils.http_status_code_to_type(http_status_code) == pyhttpstatus_utils.HttpStatusType.SUCCESSFUL.value)
            else:
                assert(pyhttpstatus_utils.http_status_code_to_type(http_status_code) != pyhttpstatus_utils.HttpStatusType.SUCCESSFUL.value)

    def test_is_http_status_type(self):
        __all_http_status_code__ = list(map(int, pyhttpstatus_utils.HttpStatusCode))
        __all_http_status_type__ = list(pyhttpstatus_utils.HttpStatusType)

        for http_status_code in __all_http_status_code__:
            for http_status_type in __all_http_status_type__:
                http_status_success = pyhttpstatus_utils.is_http_status_type(
                    http_status_code=http_status_code,
                    http_status_type=http_status_type
                )

                assert(type(http_status_success) is bool)

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