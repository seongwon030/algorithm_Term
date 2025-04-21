import time

filename = "harry_full.txt"

start_time = time.time()

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()

# 파이썬 내장 정렬 함수 사용
words.sort()  # 제자리 정렬 (리스트 자체가 정렬됨)

end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"내장 정렬 시간: {int(minutes)}분 {float(seconds)}초")
