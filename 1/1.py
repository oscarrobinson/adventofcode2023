def calibration_sum(filename):
    with open(filename) as file:
        sum = 0
        for line in file.readlines():
            first_digit = ""
            last_digit = ""
            for char in line.strip():
                if char.isdigit():
                    if first_digit == "":
                        first_digit = char
                    last_digit = char
            sum += int(first_digit + last_digit)
        return sum

def word_calibration_sum(filename):
    words_to_digits = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    words_to_digits_prefixes = set()
    for word in words_to_digits.keys():
        for i in range(0, len(word)+1):
            words_to_digits_prefixes.add(word[0:i])

    with open(filename) as file:
        sum = 0
        for line in file:
            first_digit = ""
            last_digit = ""
            for i, char in enumerate(line):
                # If char is a prefix, lookahead to see if we can consume a number word
                if char in words_to_digits_prefixes:
                    stack = char
                    for nextchar in line[i+1:len(line)]:
                        stack += nextchar
                        if stack in words_to_digits:
                            if first_digit == "":
                                first_digit = words_to_digits[stack]
                            last_digit = words_to_digits[stack]
                            # We looked ahead and found a whole digit, now we can break out of our lookahead loop
                            # We'll then go onto to start processing from the next character in the line
                            # This handles cases where we have digit names overlapping e.g twone
                            # In this case we want 1 as the last digit, not 2.
                            break
                        elif stack not in words_to_digits_prefixes:
                            break
                elif char.isdigit():
                    if first_digit == "":
                        first_digit = char
                    last_digit = char

            print(line[:-1]+": "+first_digit+" "+last_digit)
            sum += int(first_digit + last_digit)
        return sum

def test_calibration_sum():
    assert calibration_sum('./1/1_test_input.txt') == 142

def test_word_calibration_sum():
    assert word_calibration_sum('./1/1_2_test_input.txt') == 344

print(word_calibration_sum('./1/1_input.txt'))