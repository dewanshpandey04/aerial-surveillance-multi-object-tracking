from src.surveillance import _parse_class_filter


def test_parse_class_filter():
    assert _parse_class_filter("uav, vehicle ,person") == {"uav", "vehicle", "person"}


def test_parse_class_filter_empty():
    assert _parse_class_filter(None) is None
    assert _parse_class_filter("  ") is None
