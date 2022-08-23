import requests

file = open("Output.txt", "a", encoding="utf-8")
url = "https://m.diemthi.tuyensinh247.com/tracuu/ajaxDiemthiTHPT"
res = requests.post(url, data = load)
begin = 35000001 #first candidate number
end = 35013381 #last candidate number
for sbd in range(begin, end + 1):
    load = {"sbd": "{}".format(sbd)}
    res = requests.post(url, data = load)
    file.write(str(res.text.encode('utf-8')))
    file.write("\n")
