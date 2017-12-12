#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

import functools
from http import HTTPStatus

@functools.lru_cache()
def _create_http_status_code_to_phrase():
    http_status_code_to_phrase = {}

    for httpstatus in list(HTTPStatus):
        code = int(httpstatus)
        http_status_code_to_phrase[code] = httpstatus.phrase

    return http_status_code_to_phrase

HTTP_STATUS_CODE_TO_PHRASE = _create_http_status_code_to_phrase()
