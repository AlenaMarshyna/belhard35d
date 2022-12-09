import asyncio


async def foo():
    for i in range(10):
        await asyncio.sleep(1)
        print(i)


async def bar():
    for i in 'qwertyuiop':
        await asyncio.sleep(1)
        print(i)


async def main():
    tasks = [asyncio.create_task(foo()) for _ in range(100)]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
