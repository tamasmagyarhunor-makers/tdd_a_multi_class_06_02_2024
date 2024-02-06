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

"""
Given a Blender makes juice
It returns a Fruit juice.
"""
def test_blender_makes_juice():
    blender = Blender()
    fruit = Fruit('orange')
    blender.add_fruit(fruit)
    actual = blender.make_juice()
    expected = "orange juice"

    assert actual == expected

"""
Given a Blender makes juice with multiple Fruits
It returns a Fruit juice with multiple Fruits.
"""
def test_blender_makes_juice_with_2_fruits():
    blender = Blender()
    fruit = Fruit('orange')
    fruit2 = Fruit('apple')
    blender.add_fruit(fruit)
    blender.add_fruit(fruit2)
    actual = blender.make_juice()
    expected = "orange, apple juice"

    assert actual == expected