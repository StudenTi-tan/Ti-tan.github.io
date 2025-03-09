#階乗
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)
num = int(input("数値を入力してください"))
result = factorial(num)

print(f"{num}!={result}")
