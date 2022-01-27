import pytest
from convertor import convert_DD_to_DDM


@pytest.mark.parametrize(
    "DD, excepted", [
         (-180, (180, 0, 0)),
         (-180.0, (180, 0, 0)),
         (-13.912, (13, 54.72, 0)),
         (0, (0, 0, 0)),
         (180.0, (180, 0, 0)),
         (180, (180, 0, 0)),
         (170.0323, (170, 1.938, 0))
    ]
)
def test_converter(DD, excepted):
    assert convert_DD_to_DDM(DD) == excepted
