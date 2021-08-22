print("구구단 몇단을 계산할까요?")
gugu = int(input())
print(f"구구단 {gugu}단을 계산합니다.")
for i in range(1,10):
    if i>=4 and i<=7:
        if i==4:
            print("··· ··· ···")
            continue
        else:
            continue
    print(f"{gugu} X {i} = {gugu*i}")