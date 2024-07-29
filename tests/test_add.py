# tests/test_add.py
import pytest
from src.add import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(123456789, 987654321) == 1111111110
