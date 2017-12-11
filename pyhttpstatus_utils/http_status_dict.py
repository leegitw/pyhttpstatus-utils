#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import functools
from .http_status_extended import HTTPStatus

@functools.lru_cache()
def create_http_status_dict():
    http_status_dict = {}

    for httpstatus in list(HTTPStatus):
        code = int(httpstatus)
        http_status_dict[code] = {
            "code": code,
            "name": httpstatus.name,
            "phrase": httpstatus.phrase,
            "description": httpstatus.description
        }

    return http_status_dict


HTTP_STATUS_DICT = create_http_status_dict()