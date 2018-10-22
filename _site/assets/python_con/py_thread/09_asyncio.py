import asyncio

#https://asyncio.readthedocs.io/en/latest/hello_world.html

async def say(what, when):
    await asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()

loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))

pending = asyncio.Task.all_tasks()
loop.run_until_complete(asyncio.gather(*pending))

print('Main thread exit')

