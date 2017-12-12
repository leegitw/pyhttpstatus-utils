#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from pprintpp import pprint
import pyhttpstatus_utils

__all__ = list(map(int, pyhttpstatus_utils.HttpStatusCode))

for status_code in __all__:
    pprint(pyhttpstatus_utils.http_status_code_to_type(status_code))
    pprint(pyhttpstatus_utils.is_http_status_successful(status_code))

    if pyhttpstatus_utils.is_http_status_successful(status_code):
        pprint(pyhttpstatus_utils.http_status_code_to_type(status_code) == pyhttpstatus_utils.HttpStatusType.SUCCESSFUL)
    else:
        pprint(pyhttpstatus_utils.http_status_code_to_type(status_code) != pyhttpstatus_utils.HttpStatusType.SUCCESSFUL)
