"""
Encoding a value into a binary representation
based on the ordinal number of the first element encountered
"""
from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_int_raises_type_error():
    with pytest.raises(TypeError):
        fit_transform(3)


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        fit_transform(None)


def test_string():
    assert fit_transform('^') == [('^', [1])]


def test_empty_list():
    assert fit_transform([]) == []


def test_empty_list():
    assert fit_transform(['.', ',', '.']) == [('.', [0, 1]), (',', [1, 0]), ('.', [0, 1])]
