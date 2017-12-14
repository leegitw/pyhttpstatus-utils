#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

__title__ = 'pyhttpstatus-utils'
__version__ = '0.2.3'
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'MIT License'

__python_required_version__ = (3, 0)

from .http_status_dicts import (
    HTTP_STATUS_CODE_TO_PHRASE,
    HTTP_STATUS_CODE_TO_DESC,
    HTTP_STATUS_CODE_TO_TYPE,
    HTTP_STATUS_DICT
)

from .http_status_code import HttpStatusCode
from .http_status_type import HttpStatusType, HttpStatusCodeType

from .http_status_methods import (
    http_status_dict,
    http_status_code_to_desc,
    http_status_code_to_type,
    is_http_status_type,
    is_http_status_successful,
    validate_http_code
)
