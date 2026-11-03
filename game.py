import random


def get_guess():
    while True:
        text = input("حدس خود را وارد کنید (1 تا 100): ")
        try:
            number = int(text)
        except ValueError:
            print("ورودی نامعتبر! فقط عدد وارد کنید.")
            continue
        if number < 1 or number > 100:
            print("عدد باید بین 1 تا 100 باشد.")
            continue
        return number


def near_message(diff):
    if diff <= 5:
        return "خیلی نزدیکی!"
    elif diff <= 15:
        return "نزدیکی، ولی هنوز فاصله داری!"
    else:
        return "خیلی دوری!"


def get_rank(attempts):
    if attempts == 1:
        return "نمونه‌ای!"
    elif attempts == 2:
        return "بسیار خوبی!"
    elif attempts == 3:
        return "خوب"
    elif attempts == 4:
        return "قبول"
    else:
        return "با شانس بردی!"


def play():
    secret = random.randint(1, 100)
    won = False

    for attempt in range(1, 6):
        print("\nتلاش", attempt, "از 5")
        print("جان باقی‌مانده:", 5 - attempt)

        guess = get_guess()

        if guess == secret:
            won = True
            print("\nبرنده شدی! عدد مخفی", secret, "بود.")
            print("رتبه شما:", get_rank(attempt))
            break

        diff = abs(guess - secret)
        msg = near_message(diff)

        if guess > secret:
            print("کوچک‌تر وارد کن.", msg)
        else:
            print("بزرگ‌تر وارد کن.", msg)

    if not won:
        print("\nباختی! عدد مخفی", secret, "بود.")

    while True:
        answer = input("\nدوباره بازی کنی؟ (بله/خیر): ")
        if answer == "بله":
            return True
        elif answer == "خیر":
            return False
        else:
            print("لطفاً بله یا خیر بنویس.")


def main():
    print("به بازی حدس اعداد خوش آمدی!")

    while True:
        again = play()
        if not again:
            break

    print("\nخداحافظ!")


if name == "main":
    main()

