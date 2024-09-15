def increase_person_age(person):
    print(id(person))
    person['age'] +=1
    return  person


def person_name(person):
    print(id(person))
    person['name']  = "Artuom"
    return  person

person_one = {
    'name':'Bob',
    'age' :21
}
print("_________1__________-")
print(id(person_one))
increase_person_age(person_one)
print("__________2_________-")
print(id(person_one))
print(person_name(person_one))
print("__________2_________-")




print(person_one['age'])
print(id(person_one))
increase_person_age(person_one)
increase_person_age(person_one)
increase_person_age(person_one)
print(person_name(person_one))
print(person_one)


