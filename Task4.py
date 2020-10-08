def check_number(res):
    print("The original dictionary is : " + str(res))
    search_value = 200
    result = ""
    for name, simple_value in res.items():
        if simple_value == search_value:
            result = (f"Yes, value: '{search_value}' exists in dictionary")
            break
        else:
            result = (f"No, value: '{search_value}' does not exists in dictionary")
    print (result)

dict_obj = {}
while True:
    try:
        name = input("Give the key: ")
        simple_value = int(input("Give the value: "))
        dict_obj.update({(name, simple_value)})
        cont = input("Want to add another? (N or Enter)")
        if cont.lower().strip() == "n":
            break;
    except Exception as e:
        print("Something went wrong, please repeat")
check_number(dict_obj)
