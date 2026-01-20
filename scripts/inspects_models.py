import importlib, traceback
try:
    m = importlib.import_module('backend.models')
    print('MODULE FILE:', m.__file__)
    print('PUBLIC NAMES:', [k for k in m.__dict__.keys() if not k.startswith('_')])
    print('CLASS CompanyPrimary IN MODULE:', 'CompanyPrimary' in m.__dict__)
    print('\n---SOURCE---\n')
    print(open(m.__file__, 'r', encoding='utf-8').read())
except Exception:
    traceback.print_exc()