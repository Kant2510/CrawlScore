import csv
import json

input = open("raw.txt", 'r', encoding="utf-8")
file_csv = open("Output.csv", 'w', encoding="utf-8")
header = ["SBD", "Toán", "Lý", "Hóa", "Sinh", "Sử", "Địa", "GDCD", "Văn", "Ngoại ngữ", "Mã NN"]
with open("Output.csv", "a", encoding="utf-8", newline='') as file_csv:
    write = csv.writer(file_csv)
    write.writerow(header)
raw_data =  input.readlines()
for i in range(13381): #i run to number of students
    clean_data = []
    if(json.loads(raw_data[i].encode("utf-8"))["success"]):
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["candidate_number"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_toan"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_ly"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_hoa"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_sinh"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_su"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_dia"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_gdcd"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_van"])
        clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["mon_ngoaingu"])
        if json.loads(raw_data[i].encode("utf-8"))["data"]["ma_mon_ngoai_ngu"] != "":
            clean_data.append(json.loads(raw_data[i].encode("utf-8"))["data"]["ma_mon_ngoai_ngu"])
        else:
            clean_data.append("none")
    else:
        clean_data = [str(35000000 + i + 1), "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "none"] #35 is candidate number of Quang Ngai province
    with open("Output.csv", "a", encoding="utf-8", newline='') as file_csv:
        write = csv.writer(file_csv)
        write.writerow(clean_data)
