#!/usr/bin/env python

import pytest
from six import with_metaclass


def test_list_type():
    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)
    assert squares[0] == 1
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]
    assert squares[:] == [1, 4, 9, 16, 25]
    assert squares + [36, 49, 64, 81, 100] == [
        1, 4, 9, 16, 25, 36, 49, 64, 81, 100
    ]

    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64
    assert cubes == [1, 8, 27, 64, 125]
    cubes.append(216)
    cubes.append(7**3)
    assert cubes == [1, 8, 27, 64, 125, 216, 343]

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []
    assert letters == ['a', 'b', 'f', 'g']
    letters[:] = []
    assert letters == []

    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4

    list_of_chars = ['a', 'b', 'c']
    list_of_numbers = [1, 2, 3]
    mixed_list = [list_of_chars, list_of_numbers]
    assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]
    assert mixed_list[0] == ['a', 'b', 'c']
    assert mixed_list[0][1] == 'b'


def test_list_methods():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.append('grape')
    assert fruits == [
        'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape'
    ]

    fruits.remove('grape')
    assert fruits == [
        'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'
    ]

    with pytest.raises(Exception):
        fruits.remove('not existing element')

    fruits.insert(0, 'grape')
    assert fruits == [
        'grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'
    ]

    assert fruits.index('grape') == 0
    assert fruits.index('orange') == 1
    assert fruits.index('banana') == 4
    assert fruits.index('banana', 5) == 7

    with pytest.raises(Exception):
        fruits.index('not existing element')

    assert fruits.count('tangerine') == 0
    assert fruits.count('banana') == 2

    fruits_copy = fruits.copy()
    assert fruits_copy == [
        'grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'
    ]

    fruits_copy.reverse()
    assert fruits_copy == [
        'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape'
    ]

    fruits_copy.sort()
    assert fruits_copy == [
        'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear'
    ]

    assert fruits == [
        'grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'
    ]
    assert fruits.pop() == 'banana'
    assert fruits == [
        'grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple'
    ]

    fruits.clear()
    assert fruits == []


def test_del_statement():
    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    assert numbers == [1, 66.25, 333, 333, 1234.5]

    del numbers[2:4]
    assert numbers == [1, 66.25, 1234.5]

    del numbers[:]
    assert numbers == []

    del numbers
    with pytest.raises(Exception):
        assert numbers == []
