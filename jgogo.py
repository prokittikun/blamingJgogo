def jgogo(word: str) -> str:
    return f"ไอ้เจไอ้{word}"

while True:
    word = input("พิมพ์คำที่ต้องการด่าเจ : ")
    if word == "น่ารัก" or word == "หล่อ":
        break
    print(jgogo(word))