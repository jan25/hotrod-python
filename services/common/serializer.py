import json
import importlib

def obj_to_json(o):
    return obj_to_dict(o)

def json_to_obj(j):
    return dict_to_obj(j)

def obj_to_dict(o):
    obj_dict = {
        "__class__": o.__class__.__name__,
        "__module__": o.__module__
    }
    obj_dict.update(o.__dict__)
    return obj_dict

def dict_to_obj(d):
    if "__class__" in d:
        class_name = d.pop("__class__")    
        module_name = d.pop("__module__")
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        obj = class_(**d)
    else:
        obj = d
    return obj