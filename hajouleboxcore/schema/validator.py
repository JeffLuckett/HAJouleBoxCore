"""
Schema validator for HAJouleBoxCore.
Checks that entities comply with the Core Entity Schema contract.
"""

ALLOWED_UNITS = {"kW", "kWh", "%"}
ALLOWED_DEVICE_CLASSES = {"power", "energy", "battery"}
ALLOWED_STATE_CLASSES = {"measurement", "total_increasing"}

def validate_entity(entity: dict) -> bool:
    required = {"name", "value", "unit", "device_class", "state_class"}
    if not required.issubset(entity.keys()):
        return False

    if not isinstance(entity["name"], str):
        return False
    if not isinstance(entity["value"], (int, float)):
        return False
    if entity["unit"] not in ALLOWED_UNITS:
        return False
    if entity["device_class"] not in ALLOWED_DEVICE_CLASSES:
        return False
    if entity["state_class"] not in ALLOWED_STATE_CLASSES:
        return False

    return True
