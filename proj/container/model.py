import csv
import json
# kaggle 자체적으로 api 기능 구현이 다운로드 밖에 없어서 
# csv 파일을 직접 받아 처리하는 방식을 채택했습니다.
file = './data/container.csv';
json_file = './data/container.json';

#Read CSV File
def read_CSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            #csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
            json_data = {
                "pk" : "",
                "Harbor" : "",
                "Date" : "",
                "isKorean" : "",
                "empty" : {
                    "10" : "",
                    "20" : "",
                    "40" : "",
                    "other" : ""
                },
                "full" : {
                    "10" : "",
                    "20" : "",
                    "40" : "",
                    "other" : ""
                },
                "R/T" : ""
            }
            for i in range(len(field)):
                if 'pk' == field[i]:
                    json_data["pk"] = row[field[i]]
                elif 'Harbor' == field[i]:
                    json_data["Harbor"] = row[field[i]]
                elif 'Date' == field[i]:
                    json_data["Date"] = row[field[i]]
                elif 'isKorean' == field[i]:
                    json_data["isKorean"] = row[field[i]]
                elif 'Full_10' == field[i]:
                    json_data["full"]["10"] = row[field[i]]
                elif 'Full_20' == field[i]:
                    json_data["full"]["20"] = row[field[i]]
                elif 'Full_40' == field[i]:
                    json_data["full"]["40"] = row[field[i]]
                elif 'Full_other' == field[i]:
                    json_data["full"]["other"] = row[field[i]]
                elif 'Empty_10' == field[i]:
                    json_data["empty"]["10"] = row[field[i]]
                elif 'Empty_20' == field[i]:
                    json_data["empty"]["20"] = row[field[i]]
                elif 'Empty_40' == field[i]:
                    json_data["empty"]["40"] = row[field[i]]
                elif 'Empty_other' == field[i]:
                    json_data["empty"]["other"] = row[field[i]]
                elif 'R/T' == field[i]:
                    json_data["R/T"] = row[field[i]]    
            csv_rows.append(json_data)
        #convert_write_json(dict(csv_rows), json_file)
        print(csv_rows)

#Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data))

read_CSV(file,json_file)
