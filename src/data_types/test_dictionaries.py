def test_dictionary():
    """Dictionary"""

    fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

    assert isinstance(fruits_dictionary, dict)

    assert fruits_dictionary['apple'] == 'green'
    assert fruits_dictionary['banana'] == 'yellow'
    assert fruits_dictionary['cherry'] == 'red'

    assert 'apple' in fruits_dictionary
    assert 'pineapple' not in fruits_dictionary

    # Modify
    fruits_dictionary['apple'] = 'red'

    # Add
    fruits_dictionary['pineapple'] = 'yellow'
    assert fruits_dictionary['pineapple'] == "yellow"

    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
    assert sorted(fruits_dictionary) == [
        'apple', 'banana', 'cherry', 'pineapple'
    ]

    del fruits_dictionary['pineapple']
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127),
                                       ('jack', 4098)])

    assert dictionary_via_constructor['sape'] == 4139
    assert dictionary_via_constructor['guido'] == 4127
    assert dictionary_via_constructor['jack'] == 4098

    dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}

    assert dictionary_via_expression[2] == 4
    assert dictionary_via_expression[4] == 16
    assert dictionary_via_expression[6] == 36

    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)

    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098
