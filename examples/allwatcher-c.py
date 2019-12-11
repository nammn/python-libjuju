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

    facade = client.ControllerFacade.from_connection(controller.connection())
    watcherId = await facade.WatchAllModels()
    print(watcherId.watcher_id)
    while True:
        change = await watcherId.Next()
        for delta in change.deltas:
            print(delta.deltas)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Run loop until the process is manually stopped (watch will loop
    # forever).
    loop.run(watch())