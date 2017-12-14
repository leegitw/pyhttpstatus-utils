#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from pprintpp import pprint
import pyhttpstatus_utils

import os
_, tail = os.path.split(__file__)
pprint(tail)

_HTTP_STATUS_CODES_RETRY = [
    pyhttpstatus_utils.HttpStatusCode.BAD_GATEWAY,
    pyhttpstatus_utils.HttpStatusCode.SERVICE_UNAVAILABLE,
    pyhttpstatus_utils.HttpStatusCode.GATEWAY_TIMEOUT,
    pyhttpstatus_utils.HttpStatusCode.TOO_MANY_REQUESTS
]

pprint(list(map(int, _HTTP_STATUS_CODES_RETRY)))
