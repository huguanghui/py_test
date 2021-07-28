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


def test_list_comprehensions():
    squares = []
    for number in range(10):
        squares.append(number**2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    squares = list(map(lambda x: x**2, range(10)))
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    squares = [x**2 for x in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1),
                            (3, 4)]

    combinations = []
    for first_number in [1, 2, 3]:
        for second_number in [3, 1, 4]:
            if first_number != second_number:
                combinations.append((first_number, second_number))

    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1),
                            (3, 4)]

    vector = [-4, -2, 0, 2, 4]

    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -4, 0, 4, 8]

    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 2, 4]

    abs_vector = [abs(x) for x in vector]
    assert abs_vector == [4, 2, 0, 2, 4]

    fresh_fruit = ['banana', 'loganberry', 'passion fruit ']
    clean_fresh_fruit = [weapon.strip() for weapon in fresh_fruit]
    assert clean_fresh_fruit == ['banana', 'loganberry', 'passion fruit']

    square_tuples = [(x, x**2) for x in range(6)]
    assert square_tuples == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_vector = [num for elem in vector for num in elem]
    assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_nested_list_comprehensions():
    """Nested List Comprehensions

    """
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    assert transposed_matrix == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    transposed = []
    for i in range(4):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    assert list(zip(*matrix)) == [
        (1, 5, 9),
        (2, 6, 10),
        (3, 7, 11),
        (4, 8, 12),
    ]
