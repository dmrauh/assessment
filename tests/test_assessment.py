import pytest
import assessment as asmnt

from hypothesis import given
import hypothesis.strategies as st


@given(st.floats(min_value=1, max_value=5))
def test_add_grade_level(f):
    assert asmnt.add_grade_level(f) > f

