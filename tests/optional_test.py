import teext as tx


def test_optional_with_none() -> None:
    x = 3
    if x > 2:
        a = None
    else:
        a = 4
    y = tx.unwrap(a, 7)
    assert y == 7


def test_optional_with_value() -> None:
    x = 1
    if x > 2:
        a = None
    else:
        a = 4
    y = tx.unwrap(a, 7)
    assert y == 4


def test_maybe_apply() -> None:
    x = 1
    if x > 2:
        a = None
    else:
        a = 4

    def _double(b: int) -> int:
        return b * 2

    y = tx.maybe_apply(a, _double)
    assert y == 8


def test_maybe_apply_none() -> None:
    x = 3
    if x > 2:
        a = None
    else:
        a = 4

    def _double(b: int) -> int:
        return b * 2

    y = tx.maybe_apply(a, _double)
    assert y is None
