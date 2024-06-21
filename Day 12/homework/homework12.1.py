num = 1
sum_of_evens = 0

while num <= 10:
    # შეამოწმეთ არის თუ არა რიცხვი ლუწი
    if num % 2 == 0:
        # თუ რიცხვი ლუწია, დაამატეთ იგი ჯამს
        sum_of_evens += num
    # გადადით შემდეგ ნომერზე
    num += 1

# ამობეჭდეთ ლუწი რიცხვების ჯამი
print("The sum of even numbers from 1 to 10 is:", sum_of_evens)
