
def estimate_time(password):
    # Can change the value of the guesses
    guesses = 10 ** 15
    # Character sets: lowercase, uppercase, digits, and special characters
    char_sets = {
        'lowercase': 26,
        'uppercase': 26,
        'digits': 10,
        'specials': 32
    }
    # Determine which character sets are used in the password
    sets_used = {'lowercase': any(c.islower() for c in password),
                 'uppercase': any(c.isupper() for c in password),
                 'digits': any(c.isdigit() for c in password),
                 'specials': any(not c.isalnum() for c in password)}

    total_char_set_size = sum(
        size for set_name, size in char_sets.items() if sets_used[set_name])
    combinations = total_char_set_size ** len(password)
    time = combinations / guesses
    days = time // (24 * 3600)
    time = time % (24 * 3600)
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    seconds = time % 60
    if int(days) == 0 and int(hours) == 0 and int(minutes) == 0 and int(seconds) == 0:
        seconds = 1
    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"


def print_time(password):
    estimated_time_str = estimate_time(password)
    return "Estimate time to crack the password is: " + str(estimated_time_str)
