from hajouleboxcore.schema.validator import validate_entity

def test_validate_entity_minimal_valid():
    entity = {
        "name": "grid_import_kw",
        "value": 0.0,
        "unit": "kW",
        "device_class": "power",
        "state_class": "measurement",
    }
    assert validate_entity(entity)

def test_validate_entity_invalid_unit():
    entity = {
        "name": "grid_import_kw",
        "value": 0.0,
        "unit": "Watts",
        "device_class": "power",
        "state_class": "measurement",
    }
    assert not validate_entity(entity)

def test_validate_entity_missing_field():
    entity = {
        "name": "grid_import_kw",
        "value": 0.0,
        "unit": "kW",
        # device_class missing
        "state_class": "measurement",
    }
    assert not validate_entity(entity)
