"""
Regression tests targeting the specific bugs fixed in the guessing game.

check_guess returns a (outcome, message) tuple, e.g. ("Too High", "📉 Go LOWER!").
"""

from logic_utils import check_guess, get_range_for_difficulty


# --- Bug 1: the hint direction was inverted -------------------------------
# Originally a "Too High" guess told the player to "Go HIGHER!" and a
# "Too Low" guess told them to "Go LOWER!" — pointing away from the secret.
# These tests assert the MESSAGE points toward the secret, which is the part
# that was actually broken (the outcome label was already correct).

def test_too_high_tells_player_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_tells_player_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_correct_guess_wins():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


# --- Bug 2: secret was stringified on even attempts -----------------------
# The caller used to convert the secret to a str on alternating turns, so
# check_guess compared an int against a str and fell back to LEXICOGRAPHIC
# comparison. Lexicographically "9" > "100", so guessing 9 against secret 100
# wrongly reported "Too High". These cases would fail under string comparison
# but pass with correct numeric comparison.

def test_single_digit_below_three_digit_secret_is_too_low():
    # "9" > "100" as strings, but 9 < 100 as numbers.
    outcome, message = check_guess(9, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_two_digit_below_three_digit_secret_is_too_low():
    # "20" > "100" as strings, but 20 < 100 as numbers.
    outcome, message = check_guess(20, 100)
    assert outcome == "Too Low"


# --- Bug 3: difficulty range was wrong / hardcoded ------------------------
# The secret range must match the selected difficulty.

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)
