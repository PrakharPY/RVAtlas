from rvatlas.atlas.rectangle import Rectangle


def test_rectangle_intersection():

    a = Rectangle(0, 0, 64, 64)
    b = Rectangle(32, 32, 64, 64)

    assert a.intersects(b)


def test_rectangle_no_intersection():

    a = Rectangle(0, 0, 64, 64)
    b = Rectangle(128, 128, 64, 64)

    assert not a.intersects(b)