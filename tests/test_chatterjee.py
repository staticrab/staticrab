import numpy as np
import numpy.testing as nptest
from staticrab.correlation import chatterjee


def test_chatterjee_01() -> None:
    x = np.array([2.0, 5.0, 8.0, 1.0, 3.0, 1.0])
    y = np.array([7.0, 5.0, 3.0, 6.0, 7.0, 9.0])
    res = chatterjee(x, y)
    expected = 0.33333333333333337
    nptest.assert_allclose(res, expected)


def test_chatterjee_02() -> None:
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    y = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    res = chatterjee(x, y)
    expected = 0.5714285714285714
    nptest.assert_allclose(res, expected)
