i, k, guguLine = 0, 0, ""

# 구구단 2단 출력
while 2*i<10:
    guguLine += f"# {i}단\n"
    for k in range(1, 10):
        guguLine += f"{i} X {k} = {i*k}\n"
    print(guguLine)

# 구구단 3~9단 출력
while i<10:
    guguLine = ""
    for k in range(2, 10):
        guguLine += f"{i} X {k} = {i*k}\n"
    print(guguLine)