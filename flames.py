boy = ''.join(input("enters the boy's name: ").lower().strip().split())
girl = ''.join(input("enter the girl's name: ").lower().strip().split())

print(boy, girl)

let_b = set()
let_g = set()

flames = ['Friends', 'Lovers', 'Assistant', 'Marriage', 'Enemy', 'Sister']

for b in boy:
    let_b.add(b)

for g in girl:
    let_g.add(g)


flames_set_1 = let_b - let_g
flames_set_2 = let_g - let_b

flames_index = len(flames_set_1) + len(flames_set_2)

print(flames_set_1, flames_set_2, flames_index)


while len(flames) > 1:
    n = 0

    previous_index = (flames_index % len(flames) - 1) - n

    flames.remove(flames[previous_index])

    n += 1


print("your relationship is", flames[0])
