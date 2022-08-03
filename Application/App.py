from Application import export_file
import time
import random

# def start():
#     stop = False
#     while not stop:
#         data = export_file.ext_xlsx()
#         print(data)
#         for x in data:
#             print(data[x])
#         time.sleep(10)


def start() -> None:
    data = export_file.ext_xlsx()
    data_ids = [x for x in range(1, len(data)+1)]
    random.shuffle(data_ids)
    # id = random.choice(data_ids)
    for x in data_ids:
        print("Słowo: - - - - - - - - " + data[x]['Meaning'])
        user_BaseForm = input("Base Form: - - - - - - ")
        if (user_BaseForm != data[x]['BaseForm']):
            print("ŹLE! POPRAWNIE: " + data[x]['BaseForm'])
        else:
            print("Good!")
        user_PastSimple = input("Past Simple: - - - - - ")
        if (user_PastSimple != data[x]['PastSimple']):
            print("ŹLE! POPRAWNIE: " + data[x]['PastSimple'])
        else:
            print("Good!")
        user_PastParticiple = input("Past Participle: - - - ")
        if (user_PastParticiple != data[x]['PastParticiple']):
            print("ŹLE! POPRAWNIE: " + data[x]['PastParticiple'])
        else:
            print("Good!")

        input("Następne? --Enter--")
        print('\n', end='')


