import re

import pytest
from attribute_router import Chain


@pytest.fixture
def chain():
    return Chain("", {re.compile("(.*)/(TEST)$"): lambda: "SUCCESS"}, "/")


def test_chain(chain):
    """Test if chain works"""

    assert isinstance(chain.anything, Chain)


def test_deep_chain(chain):
    """Test if chain works"""

    assert isinstance(chain.anything.also_anything, Chain)


def test_call_chain(chain):
    """Test if chain __call__ works"""

    assert isinstance(chain.anything.also_anything("TEST"), Chain)


def test_chain_method(chain):
    """Test if chain returns methods when called"""

    assert callable(chain.anything.TEST)

