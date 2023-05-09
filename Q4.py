import datetime
import jdatetime

def calculate_lifetime(birth_datetime: datetime.datetime) -> float:
    """
    Calculate the total number of elapsed seconds of a person's life.
    
    Args:
        birth_datetime: A datetime object representing the person's birth date and time.
    
    Returns:
        A float representing the total elapsed seconds of the person's life.
    """
    now = datetime.datetime.now()
    elapsed_seconds = (now - birth_datetime).total_seconds()
    return elapsed_seconds

def calculate_birthday_countdown(birth_datetime: datetime.datetime) -> str:
    """
    Calculate the number of days and minutes until a person's next birthday and return a congratulatory message.
    
    Args:
        birth_datetime: A datetime object representing the person's birth date and time.
    
    Returns:
        A string with a congratulatory message and the number of days and minutes until the person's next birthday.
    """
    today = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    next_birthday = birth_datetime.replace(year=today.year)
    if next_birthday < datetime.datetime.now():
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_until_birthday = (next_birthday - today).days
    minutes_until_birthday = days_until_birthday * 24 * 60
    return f"Your next birthday is in {days_until_birthday} days ({minutes_until_birthday} minutes). Congratulations in advance!"

def convert_to_jalali(birth_datetime: datetime.datetime) -> str:
    """
    Convert a birth date from Gregorian to Jalali (Hijri) format.
    
    Args:
        birth_datetime: A datetime object representing the person's birth date and time in Gregorian format.
    
    Returns:
        A string representing the person's birth date in Jalali (Hijri) format.
    """
    j_birth_date = jdatetime.datetime.fromgregorian(datetime=birth_datetime)
    return j_birth_date.strftime('%Y/%m/%d')

# Get user input for birth date and time in the format "YYYY-MM-DD HH:MM:SS"
input_str = input("Enter your birth date and time (YYYY-MM-DD HH:MM:SS): ")

# Parse the input string into a datetime object using strptime
birth_datetime = datetime.datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")

# Calculate elapsed seconds of life and print to the console
elapsed_seconds = calculate_lifetime(birth_datetime)
print(f"Total elapsed seconds of your life: {elapsed_seconds:.0f}")

# Calculate days and minutes until next birthday and print a congratulatory message
countdown_message = calculate_birthday_countdown(birth_datetime)
print(countdown_message)

# Convert the birth date to Jalali (Hijri) format using jdatetime
jalali_birth_date = convert_to_jalali(birth_datetime)
print(f"Your birth date in Jalali format: {jalali_birth_date}")