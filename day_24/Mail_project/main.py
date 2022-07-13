## Create custom letters

letter_mode = open("./day_24/Mail_project/letter.txt", mode = "r")
model = letter_mode.read()

with open("./day_24/Mail_project/names.txt", mode="r") as file:
    for item in file:
        guest = item[:-1]

        custom_file_name = "invitation_" + guest + ".txt"
        custom_model = model.replace("[name]", guest)

        custom_letter = open("./day_24/Mail_project/" + custom_file_name, mode = "w")
        custom_letter.write(custom_model)
        custom_letter.close()

letter_mode.close()