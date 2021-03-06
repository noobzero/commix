#!/usr/bin/env python
# encoding: UTF-8

"""
This file is part of commix project (http://commixproject.com).
Copyright (c) 2014-2017 Anastasios Stasinopoulos (@ancst).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

For more see the file 'readme/COPYING' for copying permission.
"""

import base64
import urllib
from src.utils import settings

"""
Base64 all characters in a given payload.
"""

if not settings.TAMPER_SCRIPTS['base64encode']:
  settings.TAMPER_SCRIPTS['base64encode'] = True

def encode(payload):
  payload = urllib.unquote(payload)
  payload = base64.b64encode(payload)
  return payload

#eof 