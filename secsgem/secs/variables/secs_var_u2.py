#####################################################################
# secs_var_u2.py
#
# (c) Copyright 2021, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################
"""SECS 2 byte unsigned integer variable type."""

from .secs_var_number import SecsVarNumber


class SecsVarU2(SecsVarNumber):
    """
    Secs type for 2 byte unsigned data.

    :param value: initial value
    :type value: list/integer
    :param count: number of items this value
    :type count: integer
    """

    format_code = 0o52
    text_code = "U2"
    _base_type = int
    _min = 0
    _max = 65535
    _bytes = 2
    _struct_code = "H"
    preferred_types = [int]