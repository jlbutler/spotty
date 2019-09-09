# spotty
a simple playlist-generating demo service

to run...

```shell
$ python3 ./spotty.py
 * Serving Flask app "spotty" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 190-530-198
 ```

example invocation...

```shell
$ curl -iX GET http://localhost:8080/playlist/pixies
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 1276
Server: Werkzeug/0.14.1 Python/3.7.3
Date: Mon, 09 Sep 2019 19:40:29 GMT

{
  "tracks": [
    {
      "artist": "Pixies",
      "track": "Mr. Grieves"
    },
    {
      "artist": "The Jesus and Mary Chain",
      "track": "Just Like Honey"
    },
    {
      "artist": "The Velvet Underground",
      "track": "Venus In Furs"
    },
    {
      "artist": "Joy Division",
      "track": "Transmission"
    },
    {
      "artist": "Spoon",
      "track": "Inside Out"
    },
    {
      "artist": "Pavement",
      "track": "Harness Your Hopes - (B-side)"
    },
    {
      "artist": "Pixies",
      "track": "Monkey Gone to Heaven"
    },
    {
      "artist": "Echo & the Bunnymen",
      "track": "Bring on the Dancing Horses"
    },
    {
      "artist": "Sonic Youth",
      "track": "Teen Age Riot (Album Version)"
    },
    {
      "artist": "Neutral Milk Hotel",
      "track": "Oh Comely"
    },
    {
      "artist": "Pixies",
      "track": "Gouge Away"
    },
    {
      "artist": "The Modern Lovers",
      "track": "Astral Plane"
    },
    {
      "artist": "Joy Division",
      "track": "Isolation - 2007 Remaster"
    },
    {
      "artist": "Echo & the Bunnymen",
      "track": "The Killing Moon"
    },
    {
      "artist": "Yo La Tengo",
      "track": "You Can Have It All"
    }
  ]
}
```