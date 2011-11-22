# Info

Formats a text stream as JSON.  Offers additional functionality over "python -mjson.tool" 

# Examples

	> echo '[ { "foo" : "bar", "hello" : 1 }]' | python formatjson.py --indent 2

		[
		  {
		    "foo": "bar", 
		    "hello": 1
		  }
		]

	> curl http://api.twitter.com/1/statuses/public_timeline.json | python formatjson.py

		[
		    {
		        "favorited": false, 
		        "in_reply_to_user_id": null, 
		        "contributors": null, 
		        "truncated": false, 
		        "text": "IT GETS REAL NASTY !!!", 
		        "created_at": "Tue Nov 22 19:51:11 +0000 2011", 
		        "retweeted": false, 
				...
			}
		]

	> echo '{ "c" : 3, "b" : 2, "a" : 1 }' | python formatjson.py --sort-keys

		{
		    "a": 1, 
		    "b": 2, 
		    "c": 3
		}	

# Arguments

	-h, --help            show this help message and exit
	-i level, --indent level
	                      Level of indentation. Defaults to 4.
	-s, --sort-keys       Sorts output by key.
