import os
import json

def get_locator(locator_name, page, value=None):
    base_dir = os.path.dirname(__file__)
    locator_file_path = os.path.join(base_dir, page)
    print(locator_file_path)
    print(base_dir)
    if not os.path.exists(locator_file_path):
        raise FileNotFoundError(f"Locator file not found: {locator_file_path}")

    with open(locator_file_path, 'r') as file:
        locators = json.load(file)

    locator = locators.get(locator_name)
    print(locator)
    if not locator:
        raise ValueError(f"Locator '{locator_name}' not found in {page}")

    locator_type = locator['type']
    locator_value = locator['value']

    # Replace placeholder with provided value
    if value is not None:
        locator_value = locator_value.replace("${value}", str(value))

    return locator_type, locator_value