products = {
    "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk": {"quantity": 12, "price": 90},
    "bread": {"quantity": 30, "price": 40}
}
print("<<<<<<<<<<1>>>>>>>>>")
for priceItems in products.values():
    print(priceItems["price"])

print("<<<<<<<<<<2>>>>>>>>>")
for priceItems in products.values():
    print(priceItems["price"] * 1.2)
print("<<<<<<<<<<3>>>>>>>>>")
print(products)
print("<<<<<<<<<<4>>>>>>>>>")
new_dictionary = products.copy()
print(new_dictionary)
print("<<<<<<<<<<5>>>>>>>>>")
for priceGoods in new_dictionary.values():
    priceGoods["price"] *= 1.2

print(new_dictionary)

new_dictionary.pop("milk")
print(new_dictionary)

new_dictionary ["Salt"]={"quantity": 7, "price": 12}
print(new_dictionary)

summ=0
for count  in  new_dictionary.values():
    summ = summ + count["price"]*count["quantity"]
    print("Общая сумма:", summ)
print(summ)


total_sum = sum(item["price"]*item["quantity"] for item in new_dictionary.values())
print(total_sum)
print("<<<<<<<<<<<<<<<<<<<<<<<<Task # 2>>>>>>>>>>>>>>>>>>>>>>>")
keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education',
'company', 'salary']

values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890',
'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

info = dict(zip(keys,values))
print(info)

info ={}
for key, value in zip(keys,values):
    info[key] = value
print(info)

info = {key: value for key, value in zip(keys, values)}
print(info)

print("<<<<<<<<<<<<<<<<<<<<<<<<Task # 3>>>>>>>>>>>>>>>>>>>>>>>")
string="2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
new_list=list(string)

print(new_list)
for item in new_list:
    print(item)


print(new_list[0])
cipher = {
"а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
"ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
"н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
"ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
"ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}

def decrypt_message (string, cipher):
    decrypt_mess=""
    for char in string:
        if char  in cipher:
            decrypt_mess+= cipher[char]
    return decrypt_mess

decr = decrypt_message(string,cipher)
print("Decrypted_message:", decr)


def send_decrypted_message():
    input_message = input("Введите сообщение для расшифровки: ")
    decrypted = decrypt_message(input_message, cipher)
    print("Отправлено агенту:", decrypted)



send_decrypted_message()

print("<<<<<<<<<<<<<<<<<<<<<<<<Task # 4>>>>>>>>>>>>>>>>>>>>>>>")
dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству
своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей
сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.

Doc: Вес тут совершенно ни при чем. """

letter_count = {}


for char in dialog.lower():
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1
max_letter = None
max_count = 0
print(letter_count)

for letter, count in letter_count.items():
    if count > max_count:
        max_letter = letter


print("Letter with the maximum number of occurrences:", max_letter)
print("Number of occurrences:", max_count)
