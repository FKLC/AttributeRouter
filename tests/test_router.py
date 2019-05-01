import re

import pytest
from attribute_router import Router, Chain


@pytest.fixture
def router():
    return Router({re.compile("(.*)/(TEST)$"): lambda: "SUCCESS"})


def test_router(router):
    """Test if router returns chain"""

    assert isinstance(router.anything, Chain)


def test_path_and_ref(router):
    """Test if paths are correct"""

    assert router.anything._Chain__path == "/anything"
    assert router.anything.also_anything._Chain__path == "/anything/also_anything"
    assert router.anything("also_anything")._Chain__path == "/anything/also_anything"
    assert router("anything")._Chain__path == "/anything"
