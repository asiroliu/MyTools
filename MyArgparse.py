# coding=utf-8
from __future__ import unicode_literals

"""
    Name:       MyArgparse
    Author:     Andy Liu
    Email :     aisro@qq.com
    Created:    3/26/2015
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

import argparse
import logging


def parse_command_line():
    parser = argparse.ArgumentParser(prog='PROG', description='%(prog)s can ...')
    parser.add_argument('NoPre', action="store", help='help information')
    parser.add_argument('-t', action="store_true", dest='boolean_switch', default=False, help='Set a switch to true')
    parser.add_argument('-f', action="store_false", dest='boolean_switch', default=True, help='Set a switch to false')
    parser.add_argument('-s', action="store", dest='simple_value', help="Store a simple value")
    parser.add_argument('-st', action="store", dest="simple_value", type=int,
                        help='Store a simple value and define type')
    parser.add_argument('-c', action='store_const', dest='constant_value', const='value-to-store',
                        help='Store a constant value')
    parser.add_argument('-a', action='append', dest='collection', default=[], help='Add repeated values to a list')
    parser.add_argument('-A', action='append_const', dest='const_collection', const='value-1-to-append', default=[],
                        help='Add different values to list')
    parser.add_argument('-B', action='append_const', dest='const_collection', const='value-2-to-append',
                        help='Add different values to list')
    args = parser.parse_args()

    logging.debug('NoPre            = %r' % args.NoPre)
    logging.debug('simple_value     = %r' % args.simple_value)
    logging.debug('constant_value   = %r' % args.constant_value)
    logging.debug('boolean_switch   = %r' % args.boolean_switch)
    logging.debug('collection       = %r' % args.collection)
    logging.debug('const_collection = %r' % args.const_collection)

    return args


if __name__ == '__main__':
    from MyLog import init_logger

    logger = init_logger()
    parse_command_line()
