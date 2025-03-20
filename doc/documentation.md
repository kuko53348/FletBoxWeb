# documention vars

```python
# save_data
>>> self.page.session.set("save_data", self.phone_container)

# selected_in_phone_widget
>>> self.page.session.set("selected_in_phone_widget", self.phone_container)
>>> self.page.session.set("validate_click_selection_widget", False)

# tabs cotainer
>>> self.page.session.set("tabs_containers", self)
# replace and fix code if scape any caracter NoneType
>>> code_returned = serialized_data.replace("],),", "],")
```

## get attributes widget

```python
>>> class Parent:
>>>    def __init__(self):
>>>        self.parent_value = 100

>>>    def parent_method(self):
>>>        return "Parent method"

>>> class Child(Parent):
>>>    __slots__ = ['child_parent_value']  # Only allow 'value' attribute
>>>    def __init__(self):
>>>        super().__init__()  # Initialize the parent class
>>>        self.child_parent_value = 200

>>>    def child_method(self):
>>>        return "Child method"

>>> obj = Parent()
>>> obj_child = Child()
# make a class string
>>> print(repr(object)) # object to str
>>> print(eval(object))  # str to object

# Checks if an object has a specific attribute.
>>> print(hasattr(obj, 'parent_value'))  # True
>>> print(hasattr(obj, 'non_existent'))  # False

# Retrieves the parent_value of a named attribute from an object.
>>> print(getattr(obj, 'parent_value'))  # 42
>>> print(getattr(obj, 'non_existent', 'default_parent_value'))  # 'default_parent_value'

# Sets the parent_value of a named attribute on an object. If the attribute does not exist, it creates it.
>>> setattr(obj, 'parent_value', 46)
>>> print(obj.parent_value)  # 42

# Deletes a named attribute from an object.
delattr(obj, 'parent_value')
>>> print(hasattr(obj, 'parent_value'))  # False

# Checks if an object is callable (i.e., can be called like a function).
>>> print(callable(obj.parent_method))  # True
>>> print(callable(42))  # False

# Returns a list of valid attributes and methods of an object.
>>> print(dir(obj))  # ['__class__', '__delattr__', ..., 'my_method', 'parent_value']

# Returns the type of an object.
>>> print(type(42))  # <class 'int'>
>>> print(type("Hello"))  # <class 'str'>

# Checks if an object is an instance of a class or a tuple of classes.
>>> print(isinstance(obj, Parent))  # True
>>> print(isinstance(42, (int, float)))  # True

# Checks if a class is a subclass of another class.
>>> print(issubclass(Child, Parent))  # True

# Access parent attributes and methods
#>>> print(obj.parent_value)  # 100
>>> print(obj.parent_method())  # Parent method

# Access child attributes and methods
#>>> print(obj.child_value)  # 200
>>> print(obj_child.child_method())  # Child method

# Check base classes
>>> print(Child.__bases__)  # (<class '__main__.Parent'>,)

# Dynamically add a method to the class
>>> def new_method(self):
>>>    return f"Value is {self.child_parent_value}"

>>> obj_child.new_method = new_method
>>> print(obj_child.new_method(obj_child))  # Value is 42
```
