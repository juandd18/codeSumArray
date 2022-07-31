import pytest

import main


class TestMain:
    def test_only_numbers(self):
        input = [1, 2, 3, "texto"]
        real = [1, 2, 3]
        result = main.only_numbers(input)

        assert result == real

    def test_clean_input_list(self):
        input = [1, "cambio", 3, 2, 10, 7, "texto"]
        real = [1, 2, 3, 7, 10]
        result = main.clean_input_list(input)

        assert result == real

    def test_check_size_is_zero(self):
        result = main.check_size_bigger_than_zero([])
        result2 = main.check_size_bigger_than_zero([1, 2, 3])

        assert result == False
        assert result2 == True

    def test_find_pairs_minus_values(self):
        input_lst = [1, -2, -3, 7, 10]
        sum_value = -5
        input_lst = main.clean_input_list(input_lst)
        result = main.find_pairs(input_lst, [], sum_value)
        real = [(-3, -2)]

        assert result == real

    def test_find_pairs_empty(self):
        input_lst = [1, -2, -3, 7, 10]
        sum_value = 60
        input_lst = main.clean_input_list(input_lst)
        result = main.find_pairs(input_lst, [], sum_value)
        real = []

        assert result == real

    def test_find_pairs_handling_doubles(self):
        input_lst = [1, -2.5, -3, 7, 10]
        sum_value = 7
        input_lst = main.clean_input_list(input_lst)
        result = main.find_pairs(input_lst, [], sum_value)
        real = [(-3, 10)]

        assert result == real
