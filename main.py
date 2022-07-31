""" Code to find pairs of values which sum to a specific value"""

import argparse
import numbers


def only_numbers(input_data: list) -> list:
    """
    returns a list with only integer values

    :param
        input_data(list) : input list
    :return
        a new list with only numbers
    """
    return [x for x in input_data if isinstance(x, numbers.Number)]


def clean_input_list(input_data: list) -> list:
    """
    cleans the input list to sort it and avoid non numbers

    :param
        input_data(list) : input list
    :return
        a sorted list with only numbers
    """
    input_data = only_numbers(input_data)
    input_data.sort()

    return input_data


def check_size_bigger_than_zero(input_data: list) -> bool:
    """
    checks if the size of the input list is bigger than zero

    :param
        input_data(list) : input list
    :return
        True if the len of the array is bigger than one else otherwise
    """

    return bool(input_data)


def find_pairs(input_data: list, acum_values: list, sum_value: int) -> list:
    """
    finds all the pairs values to get a  sum_value using
    a recursive approach, at each iteration the input list size is decrease by one
    until the array is empty in that case we return the acum_value list tuple

    :param
        input(list) : input list with the values to search for pairs
        acum_values(list): stores the values found to be pairs
        sum_value(int): target value to find in the sum of pairs
    :return
        the acum_values list as a list of tuples
    """
    if check_size_bigger_than_zero(input_data):
        first_element = input_data[0]
        pair_value = sum_value - first_element
        input_data.pop(0)
        if pair_value in input_data:
            acum_values.append((first_element, pair_value))
            return find_pairs(input_data, acum_values, sum_value)
        return find_pairs(input_data, acum_values, sum_value)
    return acum_values


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="finds pairs in a list which sums to a specific value"
    )
    parser.add_argument(
        "--sum-value", type=int, help="sum value to search", required=True
    )
    parser.add_argument(
        "--list", nargs="+", type=int, help="list of values", required=True
    )
    args = parser.parse_args()

    input_lst = clean_input_list(args.list)

    result = find_pairs(input_lst, [], args.sum_value)

    print(result)
