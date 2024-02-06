from lib.fruit import *

"""
Given a Fruit object is instantiated
It intantiates with a name.
"""
def test_fruit_instantiates_with_name():
    fruit = Fruit('apple')

    actual = fruit.get_name() # => None
    expected = 'apple'

    assert actual == expected