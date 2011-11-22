#! /usr/bin/python

import argparse
import json
import sys

def parse_args():
	parser = argparse.ArgumentParser(description='Formats a text stream as JSON.')

	parser.add_argument("-i", "--indent", metavar="level", type=int, default=4, dest="indent", 
                        help="Level of indentation.  Defaults to 4.")
	parser.add_argument("-s", "--skip-keys", action="store_true", default=False, dest="skipkeys", 
                        help="Skip non-basic (str, unicode, int, long, float, bool, None) keys.")                        

	return parser.parse_args()

def run_filter(args):
	text = None
	level = 0

	input = sys.stdin.read()

	try:
		obj = json.loads(input)
		text = json.dumps(obj, indent=args.indent, skipkeys=args.skipkeys)
	except ValueError:
		print "Could not parse input as JSON."

	if text is not None:
		sys.stdout.write(text)

args = parse_args()
run_filter(args)