#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils
"""
HTTP Status Types
"""

import aenum
from enum import Enum

class HttpStatusType(Enum):
    """HTTP Status Code Types
    """
    pass

aenum.extend_enum(HttpStatusType, 'INFORMATIONAL', 'Informational')
aenum.extend_enum(HttpStatusType, 'SUCCESSFUL', 'Successful')
aenum.extend_enum(HttpStatusType, 'REDIRECTION', 'Redirection')
aenum.extend_enum(HttpStatusType, 'CLIENT_ERROR', 'Client Error')
aenum.extend_enum(HttpStatusType, 'SERVER_ERROR', 'Server Error')


