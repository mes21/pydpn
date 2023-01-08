from pydpn import DeeperNetwork
import json
from fixtures import *


def test_basis(logincred):

    print(logincred)
    dpn = DeeperNetwork(**logincred)
    assert dpn is not None

def test_context_manager(logincred):
    with DeeperNetwork(**logincred) as dpn:
        assert type(dpn.dashboard.memory) is int

def test_dashboard(logincred):
    dpn = DeeperNetwork(**logincred)
    d = dpn.dashboard

    # propertys
    # memory
    memory = d.memory
    assert type(memory) is int
    assert memory in range(1, 101)

    # cpu
    cpu = d.cpu
    assert type(cpu) is int
    assert cpu in range(1, 101)
