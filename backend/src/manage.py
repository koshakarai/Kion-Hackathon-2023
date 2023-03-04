""" Main management script

    Actions:
        start <host> <port> -> setup and start application
"""

import sys
import uvicorn
import colorama

try:
    from asgi import app
except ImportError as exc:
    raise ImportError("Couldn't import FastApi Instance.")


def execute(options):
    host = "127.0.0.1"
    port = 80
    uvicorn.run("manage:app", host=host, port=port, reload=True)

action_map = {
    "start": execute,
}

if __name__ == "__main__":
    colorama.init()
    
    args = sys.argv[1:]
    action = args[0]
    options = args[1:]
    print(args, action, options) # delete after tests
    
    try:
        action_map[action](options)
    except Exception as exc:
        print(exc)
        raise exc