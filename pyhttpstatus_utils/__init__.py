#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

__title__ = 'pyhttpstatus-utils'
__version__ = '0.3.0'
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'MIT License'

__python_required_version__ = (3, 0)

from .http_status_code_to_desc import HTTP_STATUS_CODE_TO_DESC
from .http_status_code_to_phrase import HTTP_STATUS_CODE_TO_PHRASE
from .http_status_code_to_type import HTTP_STATUS_CODE_TO_TYPE
from .http_status_dict import HTTP_STATUS_DICT

from .http_status_types import HttpStatusType
from .http_status_codes import HttpStatusCode, HTTP_STATUS_CODES
from .http_status_extended import (
    HTTPStatus,
    add_http_status
)

from .http_status_methods import (
    http_status_dict,
    http_status_code_to_desc,
    http_status_code_to_type,
    is_http_status_type,
    is_http_status_successful,
    validate_http_code
)
