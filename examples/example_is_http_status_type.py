#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

import http
from pprintpp import pprint
import pyhttpstatus_utils

import os
_, tail = os.path.split(__file__)
pprint(tail)

__all_http_status_codes__ = list(map(int, http.HTTPStatus))

for http_status_code in __all_http_status_codes__:
    for _, http_status_type_value in pyhttpstatus_utils.HTTP_STATUS_TYPE_DICT.items():
        http_status_success = pyhttpstatus_utils.is_http_status_type(
            http_status_code=http_status_code,
            http_status_type=http_status_type_value
        )
        pprint(
            "{}: '{}': {}".format(
                http_status_code,
                http_status_type_value,
                http_status_success
            )
        )
