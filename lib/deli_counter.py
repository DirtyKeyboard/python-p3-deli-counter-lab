#line, take_a_number_ now_serving
katz_deli = []

def line(list):
    if len(list) == 0:
        print("The line is currently empty.")
    else:
        line = ""
        i=1
        for el in list:
            if i < len(list):
                line += f'{i}. {el} '
                i+=1
            else:
                line += f'{i}. {el}'
        print(f"The line is currently: {line}")

def take_a_number(list, name):
    list.append(name)
    print(f"Welcome, {name}. You are number {len(list)} in line.")

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {list[0]}.")
        del(list[0])