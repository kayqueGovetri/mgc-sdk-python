from src.mgc.region import Region


def test_region_values():
    assert Region.BR_SE1.value == "br-se1"
    assert Region.BR_NE1.value == "br-ne-1"


def test_region_behaves_like_string_enum():
    assert str(Region.BR_SE1) == "br-se1"
    assert Region.BR_SE1 == "br-se1"
