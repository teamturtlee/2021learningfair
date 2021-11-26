import turtle as t
import time
import random

t.bgcolor("sky blue")
t.ht()
t.up()

num_times=int(t.textinput("식물 기억 게임", "몇 개의 식물로 진행하시겠습니까? (최대 5개)"))

t. write("식물 기억하기 게임을 시작합니다.", False, "center", (" ",30))

time.sleep(3)
t.clear()

plant=["코스모스", "해바라기", "개나리", "민들레", "로즈마리", "진달래", "라일락", "라벤더", "선인장", "튤립", "소나무", "감나무", "초롱꽃", "장미", "강아지풀", "은행나무"]
ran_plant=random.sample(plant, num_times)
t.write(ran_plant, False, "center", ("", 30))
time.sleep(2)
t.clear()

user_input=t.textinput("식물 기억 게임", "기억한 식물을 입력하세요")

t.write(f"정답은 {ran_plant}입니다.", False, "center", ("",30))
t.goto(0,-50)
t.write(f"입력하신 식물은 {user_input}입니다.", False, "center", ("",30))
time.sleep(3)
t.clear()

t.write("게임을 종료합니다.", False, "center", (" ",40))
