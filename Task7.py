def Divide(num1, num2):
    return num1 / num2

input_num1_msg = "enter your first num:"
input_num2_msg = "enter your secont num:"
error_msg = "You cannot divide by 0"
exit_msg = "Want to add another? (N or Enter)"
while True:
    try:
        num1=float(input(input_num1_msg))
        num2=float(input(input_num2_msg))
        result = Divide(num1, num2)
        print(result)
        cont = input(exit_msg)
        if cont.lower().strip() == "n":
            break;
    except ZeroDivisionError:
        pass
        print(error_msg)
    except Exception as e:
        print("Error: %s" % e )
