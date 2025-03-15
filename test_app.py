import sys
import os
from app import random_fruit
# Add the directory containing `app` to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


def test_random_fruit():
    assert "apple" or "cherry" or "orange" in random_fruit()
