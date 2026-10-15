from src.result_adapter import track_records_from_result


class FakeTensor:
    def __init__(self, values):
        self.values = values

    def cpu(self):
        return self

    def tolist(self):
        return self.values


class FakeBoxes:
    id = FakeTensor([12])
    xyxy = FakeTensor([[5.0, 6.0, 25.0, 30.0]])
    conf = FakeTensor([0.88])
    cls = FakeTensor([3])


class FakeResult:
    boxes = FakeBoxes()
    names = {3: "vehicle"}


def test_track_records_from_result():
    records = track_records_from_result(FakeResult())

    assert len(records) == 1
    assert records[0].track_id == 12
    assert records[0].class_id == 3
    assert records[0].class_name == "vehicle"
    assert records[0].bbox_xyxy == (5.0, 6.0, 25.0, 30.0)


def test_track_records_from_result_without_boxes():
    class EmptyResult:
        boxes = None

    assert track_records_from_result(EmptyResult()) == []
