import os
path = os.getcwd()
path_read = path + r'\STOCK_DAY_ALL_20221125.txt'
file = open(path_read,'r',encoding="utf-8")
company = {}
file_read = file.readlines()
for i in range(len(file_read)):
     file_read_row = file_read[i]
     file_split = file_read_row.split(',')
     file_split[9].strip(r"\n")
     company[file_split[0]] = file_split[1:10]
while(1):   
    index_name = input('Please enter the company index name:')
    if(index_name not in company):
        print("沒有此代碼")
        continue
    company_data = company.get(index_name,"沒有此代碼")
    look_index = int(input("1.成交價、2.成交股數、3.成交金額、4.開盤價、5.最高價、6.最低價、7.收盤價、8.漲跌價差、9.成交筆數、0.全部:"))
    match look_index:
        case 1:
            print("證券名稱:",company_data[0])
        case 2:
            print("成交股數:",company_data[1])
        case 3:
            print("成交金額:",company_data[2])
        case 4:
            print("開盤價:",company_data[3])
        case 5:
            print("最高價:",company_data[4])
        case 6:
            print("最低價::",company_data[5])
        case 7:
            print("收盤價:",company_data[6])
        case 8:
            print("漲跌價差:",company_data[7])
        case 9:
            print("成交筆數:",company_data[8])
        case 0:
            print("證券名稱:",company_data[0])
            print("成交股數:",company_data[1])
            print("成交金額:",company_data[2])
            print("開盤價:",company_data[3])
            print("最高價:",company_data[4])
            print("最低價::",company_data[5])
            print("收盤價:",company_data[6])
            print("漲跌價差:",company_data[7])
            print("成交筆數:",company_data[8])
        case _:
            print("無此代碼")
            continue



