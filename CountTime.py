# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

"""
    Name:       CountTime
    Author:     Andy Liu
    Email :     andy.liu.ud@hotmail.com
    Created:    3/24/2015
    Copyright:  All rights reserved.
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
import logging
from time import time


def count_time(func):
    def wrapped(*args, **kargs):
        begin_time = time()
        result = func(*args, **kargs)
        end_time = time()
        cost_time = end_time - begin_time
        logging.debug('Function <%s> called cost time : <%s>' % (func.__name__, cost_time))
        return result

    return wrapped


if __name__ == '__main__':
    from MyTools.MyLog import init_logger

    logger = init_logger()

    @count_time
    def test():
        print('ha')

    test()
