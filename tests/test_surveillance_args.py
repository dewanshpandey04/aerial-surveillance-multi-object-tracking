from src.class_filter import parse_class_names


def test_parse_class_names():
    assert parse_class_names("uav, vehicle ,person") == {"uav", "vehicle", "person"}


def test_parse_class_names_empty():
    assert parse_class_names(None) is None
    assert parse_class_names("  ") is None
