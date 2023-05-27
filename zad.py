from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty base")


def delete():
    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")


def change_contact(data_tuple):

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")        


def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                pass
            case "3":
                pass
            case "4":
                change_contact()
            case "5":
                delete()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()