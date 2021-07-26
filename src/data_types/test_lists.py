#!/usr/bin/env python

import pytest


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

  letters = ['a', 'b', 'c', 'd', 'e', 'f' 'g']
  letters[2:5] = ['C', 'D', 'E']
  assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
  letters[2:5] = []
  assert letters == ['a', 'b', 'f', 'g']
  letters[:] = []
  assert letters == []

  letters = ['a', 'b', 'c', 'd']
  assert len(letters) == 4
