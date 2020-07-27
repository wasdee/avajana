import pytest
from halo import Halo

from avajana.bubbling import Bubbling


@pytest.fixture
def bubling():
    return Bubbling()

def test_main(bubling):
    spinner = Halo(text='Typing', spinner='dots')
    bubling.act_typing_simple("aiusdhjashfdjo;ahodfhoawsfi", spinner.start, spinner.stop)
