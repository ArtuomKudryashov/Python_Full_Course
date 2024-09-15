def task(numb):
    ll = "<<<<<<<<<<<<<<<<<<<<<<<<<"
    rl = ">>>>>>>>>>>>>>>>>>>>>>>>>"
    t = "Task#"
    taskNumber = f"{ll}{t} {numb}{rl}"
    print(taskNumber)


def oddVsEven():
    n = int(input("Please enter a number : "))
    if n % 2 == 0:
        print(f"{n} is even")

    else:
        print(f"{n} is odd")


def weekDay():
    day = input("Please, enter weekday: ")
    if (day == "Surtaday" or day == "Sunday"):
        print("Today is weekend")
    elif (day == "Wensday"):
        print("I have a dentist appointment today at 3:30 PM.")
    elif (day == "Monday" or day == "Tuesday" or day == "Thursday" or day == "Friday"):
        print("Today weekday")
    else:
        print("Enter correct text")


def whileFunction():
    n = int(input("Please enter a number : "))
    text = input("Please, enter a text: ")
    print((('\n' + text) * n))


def count_vowels():
    message = input("Please, enter a text: ")
    vowels = 'аеёиоуыэюя'
    count = 0

    for char in message.lower():
        if char in vowels:
            count += 1

    print(count)


def sum_positive_numbers():
    total_sum = 0
    while True:
        try:
            number = int(input("Введите целое число: "))
            if number < 0:
                print(f"Сумма введенных чисел: {total_sum}")
                break
            total_sum += number
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")
            total_sum


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def list_number_divisible_by_two_numbers(n1, n2, rang):
    new_list = [x for x in range(rang) if x % n1 == 0 and x % n2 == 0]
    print(new_list)


def list_number_divisible_by_two_numbers_for(n1, n2, rang):
    numbers = []
    for x in range(rang):
        if x % n1 == 0 and x % n2 == 0:
            numbers.append(x)

    print(numbers)

#2
def filter_number_divided_two_three(l):
    sum=0
    numb = [items for items  in  l  if isinstance(items,(int,float))]
    for count in  numb:
        sum = sum + count

    print (sum)


def get_five_message():
    list_message = []
    while True:
        message = input ("Please, Speak to me: ")
        list_message.append(message)
        if len(list_message)>5:
            del(list_message[0])
        if(message == "Пока!"):
            print("Ну лфдно пока!")
            break
        print(list_message)


#4
def sorted (numbers):
    new_list=[]
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if(numbers[j]>numbers[j+1]):
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] =temp


    for i in range(len(numbers)):
        if i == len(numbers)-1 or numbers[i] != numbers[i+1]:
            new_list.append(numbers[i])

    print("Sortes List: ", numbers )
    print("Uniq element: ", new_list)