from hajouleboxcore.schema.validator import validate_entity

def test_validate_entity_minimal():
    entity = {
        "name": "grid_import_kw",
        "value": 0.0,
        "unit": "kW",
        "device_class": "power",
        "state_class": "measurement",
    }
    assert validate_entity(entity)
