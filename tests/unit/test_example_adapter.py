from adapters.example.adapter import parse

def test_parse_empty_dict():
    assert parse({}) == {}
