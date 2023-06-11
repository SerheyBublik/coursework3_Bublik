import pytest

from main import convert_date, masking_card


def test_convert_date():
    assert convert_date("2019-04-12T17:27:27.896421") == "12.04.2019"
    assert convert_date("2019-07-12T08:11:47.735774") == "12.07.2019"
    assert convert_date("2019-01-15T17:58:27.064377") == "15.01.2019"


def test_masking_card():
    assert masking_card("Счет 33407225454123927865") == "Счет **7865"
    assert masking_card("Visa Platinum 5355133159258236") == "Visa Platinum 5355 3** **** 8236"
    assert masking_card("Visa Platinum 53551331592582366") == "Visa Platinum the number is not correct"
