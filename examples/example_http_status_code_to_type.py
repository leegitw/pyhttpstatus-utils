#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from pprintpp import pprint
import pyhttpstatus_utils

import os
_, tail = os.path.split(__file__)
pprint(tail)

for status_code in pyhttpstatus_utils.HTTP_STATUS_TYPE_DICT:
    status_type = pyhttpstatus_utils.HTTP_STATUS_TYPE_DICT[status_code]
    pprint("{0}, '{1}'".format(status_code, status_type))
