#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pyhttpstatus_utils

from pprintpp import pprint
import pyhttpstatus_utils

__all__ = list(map(int, pyhttpstatus_utils.HttpStatusCode))

pprint(__all__)
