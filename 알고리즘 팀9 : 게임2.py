import random
import time

w=["해바라기", "장미", "소나무", "단풍나무", "철쭉", "진달래", "모란", "목련", "유채", "민들레", "벚나무", "개나리","카네이션", "수국", "코스모스", "구절초", "선인장", "동백나무", "강아지풀", "라벤더", "자스민", "로즈마리","캐모마일", "전나무","수련", "감나무", "배나무","밤나무", "고사리","나팔꽃"]
n=1
print("[타자게임]준비되면 엔터!")
input()
start=time.time()

q=random.choice(w)
while n <=5:
    print("*문제", n)
    print(q)
    x=input()
    if q==x:
        print("통과!")
        n=n+1
        q=random.choice(w)
    else:
        print("오타! 다시 도전!")

end=time.time()
et=end-start
et=format(et, ".2f")
print("타자 시간:", et, "초")
