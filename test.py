print("Mój pierwsyz kalkulator :P")
while True:
    # Robie u juniora
    print("pierwsza liczba")
    x = input()
    print('działanie które chcesz wykonać (x , / , - , + )')
    z = input()
    print('druga liczba')
    y = input()
    x = int(x)
    y = int(y)

    w = float()
    if z == "x":
        w = int(x*y)
    if z == "+":
        w = int(x+y)
    if z == "-":
        w = int(x-y)
    if z == "/":
        w = (x/y)
    print(x, z, y, "=", w)