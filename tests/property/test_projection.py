import hypothesis.strategies as st
import numpy as np
import pytest
from hypothesis import given, settings

from skspatial.constants import ATOL
from skspatial.objects import Vector
from tests.property.strategies import st_arrays, st_line, st_plane


@settings(deadline=None)
@pytest.mark.parametrize('name_object', ['line', 'plane'])
@given(data=st.data())
def test_project_point(data, name_object):
    """Test projecting a point onto a line or plane."""
    array = data.draw(st_arrays)

    if name_object == 'line':
        line_or_plane = data.draw(st_line())
    elif name_object == 'plane':
        line_or_plane = data.draw(st_plane())

    point_projected = line_or_plane.project_point(array)

    # The projected point should lie on the line/plane.
    assert line_or_plane.contains_point(point_projected, atol=ATOL)

    # The vector from the point to its projection
    # should be perpendicular to the line/plane.
    vector_projection = Vector.from_points(array, point_projected)

    # The distance from the point to its projection
    # should equal the distance to the line/plane.
    distance_projection = vector_projection.norm()
    distance_to_object = abs(line_or_plane.distance_point(array))
    assert np.isclose(distance_to_object, distance_projection)

    # The distance of the projection should be the
    # shortest distance from the point to the object.
    distance_points = line_or_plane.point.distance_point(array)
    assert distance_projection < distance_points or np.isclose(
        distance_projection, distance_points
    )
