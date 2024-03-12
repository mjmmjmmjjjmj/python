cars=['bmw','audi','toyota','subaru']
#cars.sort(reverse=True)
#print(cars)
#print(sorted(cars,reverse=True))
#print(cars)
#print(len(cars))
#print(cars[-1]).
for car in cars: #확장형 for문 for (int n:arr)/자바에서는 {}로 구별해줬는데
    #파이썬에서는 그냥 콜럼: 다음에 들여쓰기 해주면 그게 블럭 지정임
    print(car)
    print(f"my car is a {car}")
print("리스트 출력 완료")
for car2 in cars:
    print ("my car\n")
    for c2 in cars:
        print()  

print("for문 종료")