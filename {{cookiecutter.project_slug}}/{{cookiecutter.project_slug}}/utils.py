import importlib


def load_identifier(name):
    if '.' not in name:
        raise AttributeError(f'Invalid identifier {name}')

    module_name, identifier = name.rsplit('.', 1)
    
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as ex:
        raise AttributeError(f'Module not found {ex}') from ex
    
    return getattr(module, identifier)
