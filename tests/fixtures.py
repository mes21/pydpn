import pytest
import json


@pytest.fixture()
def logincred() -> dict:
    return json.load(open(f"c://temp/deepercred.json", "r"))
