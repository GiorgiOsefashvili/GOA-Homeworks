def time_to_words(time):
    hours_words = ["midnight", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    minutes_words = ["o'clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
                     "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", 
                     "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", 
                     "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]

    hour, minute = map(int, time.split(':'))

    if minute == 0:
        if hour == 0:
            return "midnight"
        elif hour == 12:
            return "twelve o'clock"
        else:
            return f"{hours_words[hour % 12]} o'clock"

    elif minute <= 30:
        if minute == 15:
            minute_word = "quarter"
        elif minute == 30:
            minute_word = "half"
        else:
            minute_word = minutes_words[minute]

        if hour == 0:
            if minute == 1:
                return f"{minute_word} minute past midnight"
            else:
                return f"{minute_word} minutes past midnight"
        else:
            if minute == 1:
                return f"{minute_word} minute past {hours_words[hour % 12]}"
            else:
                return f"{minute_word} minutes past {hours_words[hour % 12]}"

    else:
        remaining_minutes = 60 - minute
        if remaining_minutes == 15:
            minute_word = "quarter"
        else:
            minute_word = minutes_words[remaining_minutes]

        next_hour = (hour + 1) % 24
        if next_hour == 0:
            next_hour_word = "midnight"
        else:
            next_hour_word = hours_words[next_hour % 12]

        if remaining_minutes == 1:
            return f"{minute_word} minute to {next_hour_word}"
        else:
            return f"{minute_word} minutes to {next_hour_word}"

# Test cases
print(time_to_words("13:00"))  # one o'clock
print(time_to_words("13:09"))  # nine minutes past one

