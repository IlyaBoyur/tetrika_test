import pytest

from task1 import task


@pytest.mark.parametrize(
    'array, expected',
    (['111111111110000000000000000', 'OUT: 11'],
     ['111111111111111111111111110', 'OUT: 26'],
     ['1111111111111111111111111110', 'OUT: 27'],
     ['11111111111111111111111111100', 'OUT: 27'],
     ['10', 'OUT: 1'],
     ['110', 'OUT: 2'],
     ['1100000000000000000000000000', 'OUT: 2'],
     ['11000000000000000000000000000', 'OUT: 2'],
     ['111110', 'OUT: 5'],
     ['100000000', 'OUT: 1'],)
)
def test_task1(array, expected):
    assert task(array) == expected
