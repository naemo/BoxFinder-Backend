# kaggle 자체적으로 api 기능 구현이 다운로드 밖에 없어서 
# csv 파일을 직접 받아 처리하는 방식을 채택했습니다.
import csv
with open('./data/container.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count = 0
    for row in data:
        count += 1
print(count)
list = []