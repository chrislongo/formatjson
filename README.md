# Info

Formats a text stream as JSON.  Offers functionality over "python -mjson.tool" 

# Examples

	echo "[ { \"foo\" : \"bar\", \"hello\" : 1 }]" | python formatjson.py --indent 2

	curl http://api.twitter.com/1/statuses/pblic_timeline.json | python formatjson.py

# Arguments

	  -h, --help            show this help message and exit
	  -i level, --indent level
	                        Level of indentation. Defaults to 4.
	  -s, --skip-keys       Skip non-basic (str, unicode, int, long, float, bool,
	                        None) keys.