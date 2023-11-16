import pytest
import urllib.request
from what_is_year_now import what_is_year_now
from unittest.mock import patch
from io import StringIO


def test_format_yyyy_mm_dd():
    """
    Test checks date format: YYYY-MM-DD
    """
    date = StringIO('{"currentDateTime": "1980-01-01"}')
    expected = 1980
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
        assert expected == actual


def test_format_dd_mm_yyyy():
    """
    Test checks date format: DD-MM-YYYY
    """
    date = StringIO('{"currentDateTime": "01.01.1980"}')
    expected = 1980
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
        assert expected == actual


def test_invalid_data():
    """
    Test checks date is not valid
    """
    date = StringIO('{"currentDateTime": "ast$@%ro098123"}')
    with pytest.raises(ValueError):
        with patch.object(urllib.request, 'urlopen', return_value=date):
            what_is_year_now()


def test_no_date_at_all():
    """
    Test checks json format with no date at all
    """
    date = StringIO('{"Russia": "Moscow"}')
    with pytest.raises(KeyError):
        with patch.object(urllib.request, 'urlopen', return_value=date):
            what_is_year_now()
