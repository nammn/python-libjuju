"""
This example:

1. Connects to the current model
2. Starts an AllWatcher
3. Prints all changes received from the AllWatcher
4. Runs forever (kill with Ctrl-C)

"""
import logging

from juju import loop
from juju.client import client
from juju.model import Model
from juju.client.connection import Connection


async def watch():
    model = Model()
    await model.connect()
    conn = model.connection()
    allwatcher = client.AllWatcherFacade.from_connection(conn)
    while True:
        change = await allwatcher.Next()
        for delta in change.deltas:
            print("")
            print("\u2665 one delta \u2665")
            print("")
            print(delta.deltas)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    # Run loop until the process is manually stopped (watch will loop
    # forever).
    loop.run(watch())
