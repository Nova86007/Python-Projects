#1405/08/21 (Written by AI)
def draw_shape(choice):
    """بر اساس عدد ورودی، یکی از ۵ شکل را با for و if چاپ می‌کند."""
    if choice == 1:
        # مثلث راست‌گوشه
        for i in range(1, 6):
            for j in range(i):
                print("*", end=" ")
            print()
    elif choice == 2:
        # مربع توخالی
        for i in range(5):
            for j in range(5):
                if i == 0 or i == 4 or j == 0 or j == 4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == 3:
        # لوزی
        for i in range(5):
            for j in range(5 - i - 1):
                print(" ", end=" ")
            for j in range(2 * i + 1):
                print("*", end=" ")
            print()
        for i in range(4 - 1, -1, -1):
            for j in range(5 - i - 1):
                print(" ", end=" ")
            for j in range(2 * i + 1):
                print("*", end=" ")
            print()
    elif choice == 4:
        # قلب 
        for raw in range(6):
            for col in range(7):
                if ((raw == 0 and col % 3 != 0) or
                    (raw == 1 and col % 3 == 0) or
                    (raw - col == 2) or
                    (raw + col == 8)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == 5:
        # مثلث متساوی‌الساقین
        for i in range(5):
            for j in range(5 - i - 1):
                print(" ", end=" ")
            for j in range(2 * i + 1):
                print("*", end=" ")
            print()


# حلقه نامعین اصلی
while True:
    print("\n" + "=" * 30)
    user_input = input("Type something between 1 to 5 (or 'q' to quit): ")

    # شرط خروج
    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    # اعتبارسنجی ورودی
    if not user_input.isdigit():
        print("Please enter a number!")
        continue

    choice = int(user_input)

    if 1 <= choice <= 5:
        print(f"\n--- Shape {choice} ---\n")
        draw_shape(choice)   # حلقه for داخل این تابع اجرا می‌شود
    else:
        print("Out of range! Try again.")
