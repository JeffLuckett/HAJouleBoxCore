"""
Schema validator for HAJouleBoxCore.
Checks that entities comply with the Core Entity Schema contract.
"""

def validate_entity(entity: dict) -> bool:
    required = {"name", "value", "unit", "device_class", "state_class"}
    return required.issubset(entity.keys())
