#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)


from collections import defaultdict
from pprintpp import pprint
import pyhttpstatus_utils

import os
_, tail = os.path.split(__file__)
pprint(tail)

_http_status_dict = defaultdict(
    lambda: 'partner returned non-200 status code', pyhttpstatus_utils.create_http_status_dict({
        401: 'Invalid api_key'
    })
)

pprint(_http_status_dict[200])
pprint(_http_status_dict[502])
pprint(_http_status_dict[401])
pprint(_http_status_dict[600])
