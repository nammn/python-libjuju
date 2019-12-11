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
from juju.controller import Controller


async def watch():
    controller = Controller()
    await controller.connect()
    conn = controller.connection()
    facade = client.ControllerFacade.from_connection(conn)
    watcher_id = await facade.WatchAllModels()
    w_id = watcher_id.watcher_id
    allwatcher = client.AllModelWatcherFacade.from_connection(conn)
    allwatcher.id = w_id
    while True:
        # TODO: find out what to do with the watcher_id
        change = await allwatcher.Next(w_id)
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
