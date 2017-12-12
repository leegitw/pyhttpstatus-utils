#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from pprintpp import pprint
import pyhttpstatus_utils

for status_code in pyhttpstatus_utils.HTTP_STATUS_CODE_TO_TYPE:
    status_type = pyhttpstatus_utils.HTTP_STATUS_CODE_TO_TYPE[status_code]
    pprint("{0}, '{1}'".format(status_code, status_type))
