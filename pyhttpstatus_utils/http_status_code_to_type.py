#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from .http_status_types import HttpStatusType

HTTP_STATUS_CODE_TO_TYPE = {
    100: HttpStatusType.INFORMATIONAL,
    200: HttpStatusType.SUCCESSFUL,
    300: HttpStatusType.REDIRECTION,
    400: HttpStatusType.CLIENT_ERROR,
    500: HttpStatusType.SERVER_ERROR
}
