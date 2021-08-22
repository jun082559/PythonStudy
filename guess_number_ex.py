import random

true_value = random.randint(1,100)
print("숫자를 맞춰보세요(1~100)")

guess = int(input())
while guess != true_value:
    if guess > true_value:
        print("Down!")
    else:
        print("UP!")
    guess = int(input())
print("Good")
print(f"정답은 {guess}")