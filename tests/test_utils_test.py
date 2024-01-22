import numpy as np

from utils.test import dict_to_str


def test_dict_to_str():
    assert dict_to_str({}) == ""

    _dict = {",fk,zkl,dc": 32, "5": np.array([2, 3, 5]), "__h": "nfnru"}

    assert dict_to_str(_dict) == ",fk,zkl,dc325[2 3 5]__hnfnru"
