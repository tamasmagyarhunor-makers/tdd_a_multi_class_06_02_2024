from lib.blender import *
from lib.fruit import *

"""
Given a Blender object is instantiated
It intantiates with an empty list.
"""
def test_blender_instantiates_with_empty_storage():
    blender = Blender()

    actual = blender.storage
    expected = []

    assert actual == expected

"""
Given a Blender adds a Fruit in the storage
The storage will contain the Fruit.
"""
def test_blender_adds_fruit():
    blender = Blender()
    fruit = Fruit('orange')
    blender.add_fruit(fruit)
    actual = blender.storage
    expected = [fruit]

    assert actual == expected
    assert type(actual[0]) == Fruit