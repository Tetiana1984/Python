import math
welcome_msg = "Enter the side "
error_msg = "Error: Please try one again or type Stop to exti from application"
exit_from_program = "stop"
triangile_aria_result = "Triangl aria is %s "
while True:
    try:
        a = input(welcome_msg).lower().strip()
        b = input(welcome_msg).lower().strip()
        c = input(welcome_msg).lower().strip()
        if a == exit_from_program or b == exit_from_program or c == exit_from_program:
            break
        else:
            a = float(a)
            b = float(b)
            c = float(c)
            p = (a + b + c) / 2
            result = math.sqrt(abs(p * (p - a) * (p - b) * (p - c)))
            print(triangile_aria_result % (result))
    except Exception as e:
        print(error_msg)
