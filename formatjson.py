#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import json
import sys
import re

def parse_args():
    parser = argparse.ArgumentParser(
        description='Formats a text stream as JSON.')

    parser.add_argument(
        '-i','--indent',
        metavar='level',
        type=int,
        default=4,
        dest='indent',
        help='level of indentation (default 4)')
    
    parser.add_argument(
        '-c','--item-separator',
        metavar='separator',
        default=',',
        dest='item_separator',
        help='dictionary seperator (default \',\')')   

    parser.add_argument(
        '-d','--dict-separator',
        metavar='separator',
        default=':',
        dest='dict_separator',
        help='dictionary seperator (default \':\')')   

    parser.add_argument(
        '-s','--sort-keys',
        action='store_true',
        default=False,
        dest='sort_keys',
        help='sorts output by key')
        
    parser.add_argument(
        '-w','--strip-whitespace',
        action='store_true',
        default=False,
        dest='strip_whitespace',
        help='remove whitespace from output (compact JSON)')              

    return parser.parse_args()

def run_filter(args):
    text = None

    input = sys.stdin.read()

    try:
        obj = json.loads(input)
        
        text = json.dumps(
            obj, 
            indent=args.indent, 
            sort_keys=args.sort_keys,
            separators=(args.item_separator, args.dict_separator))
    
    except ValueError:
        print 'Could not parse input as JSON.'

    if args.strip_whitespace:
        pattern = re.compile(r'\s+')
        text = re.sub(pattern, '', text)

    if text is not None:
        sys.stdout.write(text)

args = parse_args()
run_filter(args)