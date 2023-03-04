""" Main management script

    Actions:
        start <host> <port> -> setup and start application
"""

import sys

import typing
import colorama

import uvicorn

import config


try:
    from asgi import app
except ImportError as exc:
    raise ImportError("Couldn't import FastApi Instance.")


def start(options: typing.List[str]) -> None:
    """ Start fastapi on uvicorn asgi web server

    Args:
        options (typing.List[str]): a list containing the host and port. Implicit default ["127.0.0.1", "80"]
    """    
    
    host, port = options if options else [ "127.0.0.1", "80" ]
    port = int(port)
    
    uvicorn.run("manage:app", host=host, port=port, reload=config.RELOAD)

action_map = {
    "start": start,
}

if __name__ == "__main__":
    colorama.init()
    
    args = sys.argv[1:]
    action = args[0]
    options = args[1:]

    try:
        action_map[action](options)
    except Exception as exc:
        print(exc)
        raise exc