
def calculate(n):
    price = float(n*5)
    print("%0.3fkg을 절약함으로써 %0.2f원을 적립해드렸습니다." %(n,price))

n = float(input('탄소배출이 몇 kg인지 입력해주세요 \n'))
calculate(n)

x = input()