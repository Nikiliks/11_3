import sys
class SomeClass:

    def __init__(self):
        self.attribute = 50

def introspection_info(obj):
    info = []
    info.append(type(obj))
    info.append(hasattr(obj, "attribute"))
    info.append(getattr(obj, "attribute"))
    info.append(sys.path)
    return info

some_object = SomeClass()

number_info = introspection_info(some_object)
print(number_info)