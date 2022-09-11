from posixpath import dirname
from solid_couscous.app import game, rate, collect, ordering, Performance
from collections import Counter
import pytest
import os.path

def test_game():
    line = "Lions 3, Snakes 3"
    assert (("Lions", 3), ("Snakes", 3)) == game(line)

def test_rate():
    line = "Lions 3, Snakes 3"
    assert (("Lions", 1), ("Snakes", 1)) == rate(game(line))

def test_collect():
    line = "Lions 3, Snakes 3"
    assert Counter(Lions=1, Snakes=1) == collect(rate(game(line)))


@pytest.fixture
def lines():
    data = os.path.join(dirname(__file__), "input.txt")
    with open(data, mode="r") as f:
        rs = f.readlines()
    return rs


def test_ordering(lines):
    counter = Counter()
    for line in lines:
        collect(rate(game(line)), collection=counter)
    assert [
        Performance("Tarantulas", 6), 
        Performance("Lions", 5 ),
        Performance("FC Awesome", 1), 
        Performance("Snakes", 1), 
        Performance("Grouches", 0) 
    ] == ordering(counter)