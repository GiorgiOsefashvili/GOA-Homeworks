# შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი (დასერჩეთ python array append). ბოლოს დაპტინტეთ თქვენთვის სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.
new_numbers = []
for num in range(50, 101):
    new_numbers.append(num)

print(new_numbers[-5:])
