import asyncio
import time
import pytest
from halo import Halo

from avajana.bubbling import Bubbling


@pytest.fixture
def bubling():
    return Bubbling()


def test_main(bubling):
    print("starting in ..")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    spinner = Halo(text="Typing", spinner="dots")
    text_sample = (
        "Accept that because we were born with nothing, we can become anything!"
    )

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            bubling.act_typing(text_sample, spinner.start, spinner.stop)
        )
    finally:
        loop.close()
    print()
    print(text_sample)
    print()
