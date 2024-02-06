# {{Blender}} Class Design Recipe
## {{Fruit}} Class Design Recipe
Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
```
As a Blender
So that I can make juice
I want to be able to make juice with Fruits.
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
class Belnder():
    def __init__(self):
        self.storage = []

    def add_fruit(self, fruit):
        """It takes a fruit, and stores it in the storage.

        Parameters: (list all parameters and their types)
            fruit: a Fruit object

        Returns: (state the return value and its type)
            Nothing (None)

        Side effects: (state any side effects)
            It adds the item into the self.storage
        """
        pass # Test-driving means _not_ writing any code here yet.

    def make_juice(self, fruit):
        """It takes a Fruit, and returns a {Fruit.name} juice.

        Parameters: (list all parameters and their types)
            fruit: a Fruit object

        Returns: (state the return value and its type)
            String (eg. "Orange juice")

        Side effects: (state any side effects)
            None
        """
        pass # Test-driving means _not_ writing any code here yet.

class Fruit():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a Blender object is instantiated
It intantiates with an empty list.
"""
blender = Blender()

actual = blender.storage
expected = []

assert actual == expected


"""
Given a Blender puts a Fruit in the storage
The storage will contain the Fruit.
"""
blender = Blender()
fruit = Fruit('orange')
blender.add_fruit(fruit)
actual = blender.storage
expected = [fruit]

assert actual == expected
assert type(actual[0]) == Fruit

"""
Given a Fruit object is instantiated
It intantiates with a name.
"""
fruit = Fruit('apple')

actual = fruit.get_name()
expected = 'apple'

assert actual == expected


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE



```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
