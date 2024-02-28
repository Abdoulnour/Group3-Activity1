def check_guess(guess, answer):
    if guess==answer:
        return 0
    else:
        return None
    
def test_check_guess():
    assert check_guess(7,7)==0
