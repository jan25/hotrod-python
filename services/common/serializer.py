import json
import importlib

def obj_to_json(o):
    # return json.dumps(o, default=obj_to_dict)
    return obj_to_dict(o)

def json_to_obj(j):
    # _dict = json.loads(j)
    return dict_to_obj(j)

def obj_to_dict(o):
    #  Populate the dictionary with object meta data 
    obj_dict = {
        "__class__": o.__class__.__name__,
        "__module__": o.__module__
    }
    
    #  Populate the dictionary with object properties
    obj_dict.update(o.__dict__)

    return obj_dict

def dict_to_obj(d):
    """
    Function that takes in a dict and returns a custom object associated with the dict.
    This function makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in d:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = d.pop("__class__")
        
        # Get the module name from the dict and import it
        module_name = d.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = importlib.import_module(module_name)
        
        # Get the class from the module
        class_ = getattr(module, class_name)
        
        # Use dictionary unpacking to initialize the object
        obj = class_(**d)
    else:
        obj = d
    return obj