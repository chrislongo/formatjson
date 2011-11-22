#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import json
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description='Formats a text stream as JSON.')

    parser.add_argument(
        '-i','--indent',
        metavar='level',
        type=int,
        default=4,
        dest='indent',
        help='Level of indentation.  Defaults to 4.')
    
    parser.add_argument(
        '-s','--sort-keys',
        action='store_true',
        default=False,
        dest='sort_keys',
        help='Sorts output by key.')

    return parser.parse_args()

def run_filter(args):
    text = None

    input = sys.stdin.read()

    try:
        obj = json.loads(input)
        text = json.dumps(obj, indent=args.indent, sort_keys=args.sort_keys)
    except ValueError:
        print 'Could not parse input as JSON.'

    if text is not None:
        sys.stdout.write(text)

args = parse_args()
run_filter(args)