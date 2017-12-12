#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

from http import HTTPStatus


def add_http_status(name, value, phrase, description=''):
    # call our new member factory, it's essentially the `HTTPStatus.__new__` method
    new_status = HTTPStatus.__new_member__(HTTPStatus, value, phrase, description)
    new_status._name_ = name  # store the enum's member internal name
    new_status.__objclass__ = HTTPStatus.__class__  # store the enum's member parent class
    setattr(HTTPStatus, name, new_status)  # add it to the global HTTPStatus namespace
    HTTPStatus._member_map_[name] = new_status  #  add it to the name=>member map
    HTTPStatus._member_names_.append(name)  # append the names so it appears in __members__
    HTTPStatus._value2member_map_[value] = new_status  # add it to the value=>member map


add_http_status(
    'SWITCH_PROXY',
    306,
    'Switch Proxy',
    'No longer used. Requested resource may only be accessed through a given proxy.'
)
add_http_status(
    'UNAVAILABLE_FOR_LEGAL_REASONS',
    451,
    'Unavailable For Legal Reasons',
    'You attempted to access a Legally-restricted Resource. This could be due to censorship or government-mandated blocked access.'
)
add_http_status(
    'BANDWIDTH_LIMIT_EXCEEDED',
    509,
    'Bandwidth Limit Exceeded',
    'Bandwidth Limit Exceeded'
)
add_http_status(
    'NETWORK_READ_TIMEOUT',
    598,
    'Network Read Timeout',
    'Network Read Timeout'
)
add_http_status(
    'NETWORK_CONNECT_TIMEOUT',
    599,
    'Network Connect Timeout',
    'Network Connect Timeout'
)
