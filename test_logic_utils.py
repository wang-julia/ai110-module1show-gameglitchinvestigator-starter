import pytest
from logic_utils import check_guess

def test_check_guess_win():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

def test_check_guess_too_high():
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")

def test_check_guess_too_low():
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")

def test_check_guess_boundary_low():
    # Guess of 1 when secret is 1 should win
    assert check_guess(1, 1) == ("Win", "🎉 Correct!")

def test_check_guess_boundary_high():
    # Guess of 100 when secret is 100 should win
    assert check_guess(100, 100) == ("Win", "🎉 Correct!")

def test_check_guess_one_off_high():
    # Guess is just 1 above secret
    assert check_guess(51, 50) == ("Too High", "📉 Go LOWER!")

def test_check_guess_one_off_low():
    # Guess is just 1 below secret
    assert check_guess(49, 50) == ("Too Low", "📈 Go HIGHER!")

def test_check_guess_invalid_input():
    # Non-integer input should raise a TypeError (parse_guess handles validation, not check_guess)
    with pytest.raises(TypeError):
        check_guess("fifty", 50)