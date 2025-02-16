import json
with open("student.json", "r") as student_info:
    student_bio = json.load(student_info)
    student_fname = student_bio["first_name"]
    student_lname = student_bio["last_name"] 
    student_bgrade = student_bio["courses"][0]["grade"]
    student_country= student_bio['address']["country"]
    print(f"{student_fname} {student_lname} best grade is {student_bgrade} and is from {student_country}")


with open(r"store_data.json", "r") as product:
    data = json.load(product)
    get_brand = data["store"]["departments"][0]["categories"][1]["products"][1]["brand"]
    get_name = data["store"]["departments"][0]["categories"][1]["products"][1]["name"]
    print(f"{get_brand} {get_name}")