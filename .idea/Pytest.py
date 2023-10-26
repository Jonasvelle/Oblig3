from testing_cool import isLeapYear


def test_leap_year_divided_by_4_not_by_100():
    assert isLeapYear(2020) == True


def test_leap_year_divided_by_400():
    assert isLeapYear(2000) == True


def test_not_leap_year_not_divided_by_4():
    assert isLeapYear(2023) == False


def test_not_leap_year_divided_by_100_not_by_400():
    assert isLeapYear(1900) == False


"""
Tester om disse 4 testene nedenfor feiler for å se om funksjonen og testingen fungerer. Dette gjør jeg vet å bytte 
True og False med samme funksjon og samme år for å sjekka at testen faktisk plukker det opp, og viser til at det feiler
"""


def test_not_leap_year_divided_by_4_not_by_100():
    assert isLeapYear(2020) == False


def test_not_leap_year_divided_by_400():
    assert isLeapYear(2000) == False


def test_leap_year_not_divided_by_4():
    assert isLeapYear(2023) == True


def test_leap_year_divided_by_100_not_by_400():
    assert isLeapYear(1900) == True


"""
For å få testet dette så skriver man hvor denne filten er lagret på maskinen. Vi setter cd foran, også filveien.
Etter man har funnet filveien så skriver man: pytest Pytest.py, hvor Pytest.py er filnavnet
"""