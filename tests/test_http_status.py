#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

from collections import defaultdict
from pyhttpstatus_utils import http_status_dict


class TestHttpStatus():

    def test_status(self):
        msg_unexpected_status = 'Partner returned non-200 status code'

        _http_status_dict = defaultdict(
            lambda: msg_unexpected_status, http_status_dict({
                401: 'Invalid api_key'
            })
        )

        assert(_http_status_dict[200] == 'OK')
        assert(_http_status_dict[502] == 'Bad Gateway')
        assert(_http_status_dict[401] == 'Unauthorized: Invalid api_key.')
        assert(_http_status_dict[600] == msg_unexpected_status)
