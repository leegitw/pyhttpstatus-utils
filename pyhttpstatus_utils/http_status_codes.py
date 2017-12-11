#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils
"""
HTTP Status Codes
"""

import functools
import aenum
from enum import IntEnum
from .http_status_extended import HTTPStatus

class HttpStatusCode(IntEnum):
    """HTTP Status Codes
    """
    pass

@functools.lru_cache()
def _create_http_status_code_to_phrase():
    for httpstatus in list(HTTPStatus):
        aenum.extend_enum(HttpStatusCode, httpstatus.name, int(httpstatus))


_create_http_status_code_to_phrase()

HTTP_STATUS_CODES = list(map(int, HttpStatusCode))
