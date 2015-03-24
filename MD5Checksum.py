# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

"""
    Name:       MD5Checksum
    Author:     Andy Liu
    Email :     anx.liu@intel.com
    Created:    3/24/2015
    Copyright:  Copyright ©Intel Corporation. All rights reserved.
    Licence:    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public License 
    as published by the Free Software Foundation, either version 3 of 
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import hashlib
import os
import logging


def md5_checksum(file_path):
    logging.debug('processing %s' % file_path)
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as fh:
            m = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
        return m.hexdigest()
    else:
        return None
