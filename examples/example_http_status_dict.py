#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from pprintpp import pprint
from collections import defaultdict
import pyhttpstatus_utils

import os
_, tail = os.path.split(__file__)
pprint(tail)

__all__ = pyhttpstatus_utils.create_http_status_dict()
_HTTP_STATUS_DICT = defaultdict(lambda: 'Partner returned non-200 status code.', __all__)

for status_code in __all__:
    pprint(_HTTP_STATUS_DICT[status_code])

__all__ = list(map(int, pyhttpstatus_utils.HTTP_STATUS_DICT))
for status_code in __all__:
    pprint(status_code)

pprint(__all__)
