# score_manager.py
def save_winner_score(winner, score):
    with open("winner_score.txt", "w") as file:
        file.write(f"ผู้ชนะ: {winner}\n")
        file.write(f"สกอร์: {score}\n")

def read_winner_score():
    try:
        with open("winner_score.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "ยังไม่มีข้อมูลผู้ชนะ"
