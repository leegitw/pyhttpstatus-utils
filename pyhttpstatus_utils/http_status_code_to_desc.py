#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

import functools
from .http_status_extended import HTTPStatus

@functools.lru_cache()
def _create_http_status_code_to_desc():
    http_status_code_to_desc = {}

    for httpstatus in list(HTTPStatus):
        code = int(httpstatus)
        http_status_code_to_desc[code] = httpstatus.description

    return http_status_code_to_desc


HTTP_STATUS_CODE_TO_DESC = _create_http_status_code_to_desc()
