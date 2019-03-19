from hypothesis import given, settings

from skspatial.constants import ATOL
from skspatial.objects import Point, Points, Line
from tests.property.strategies import st_arrays


@settings(deadline=None)
@given(st_arrays, st_arrays, st_arrays)
def test_are_collinear(array_a, array_b, array_c):

    assert Points([array_a, array_a, array_a]).are_collinear(tol=ATOL)
    assert Points([array_a, array_a, array_b]).are_collinear(tol=ATOL)

    all_different = not (
        Point(array_a).is_close(array_b, atol=ATOL)
        or Point(array_b).is_close(array_c, atol=ATOL)
    )

    if Points([array_a, array_b, array_c]).are_collinear() and all_different:

        line_ab = Line.from_points(array_a, array_b)
        line_bc = Line.from_points(array_b, array_c)

        assert line_ab.contains_point(array_c, atol=ATOL)
        assert line_bc.contains_point(array_a, atol=ATOL)

        assert line_ab.is_coplanar(line_bc)
