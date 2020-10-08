def Words(_lengh, _string_tocheck):
    result =''
    for line in _string_tocheck:
        if len(line)>_lengh:
            result = result + line + ", "
    print (result)

input_msg_text = "Type test for cheking: "
input_msg_lengh = "Define lenght: "
exit_msg = "Want to add another? (N or Enter)"
while True:
    try:
        string_to_check = input(input_msg_text)
        lenght = int(input(input_msg_lengh))
        Words(lenght,string_to_check.split())
        cont = input(exit_msg)
        if cont.lower().strip() == "n":
            break;
    except Exception as e:
        print("Error: %s" % e )
