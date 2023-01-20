import asyncio
import aioconsole
import warnings
import time
warnings.filterwarnings("ignore")

t_v = 180


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


async def main__(main_loop, ts):
    t = main_loop.create_task(aioconsole.ainput("to make payment, enter here yes otherwise no>>"))
    try:
        await asyncio.wait_for(t, timeout=ts)
        value = t.result()
    except asyncio.TimeoutError as _:
        value = "Now extending payment time"
    # print(value)
    return value


async def main__2(main_loop, ts):
    t2 = main_loop.create_task(aioconsole.ainput("Time extended for 5 more minutes, now to make payment, enter yes>>"))
    try:
        await asyncio.wait_for(t2, timeout=ts)
        value = t2.result()
    except asyncio.TimeoutError as _:
        value = "Now exiting the program as time has ran out"
    # print(value)
    return value


