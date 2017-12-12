#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from pprintpp import pprint
import pyhttpstatus_utils

__all_http_status_code__ = list(map(int, pyhttpstatus_utils.HttpStatusCode))
__all_http_status_type__ = list(pyhttpstatus_utils.HttpStatusType)

for http_status_code in __all_http_status_code__:
    for http_status_type in __all_http_status_type__:
        http_status_success = pyhttpstatus_utils.is_http_status_type(
            http_status_code=http_status_code,
            http_status_type=http_status_type
        )
        pprint(
            "{}:{}:'{}':{}".format(
                http_status_code,
                http_status_type.name,
                http_status_type.value,
                http_status_success
            )
        )
