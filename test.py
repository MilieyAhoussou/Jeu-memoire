import fonctions
import json
score = fonctions.charger_score()
print(score)

score = [{"Pseudo" : "Miliey","Score" : 200,"Difficulté" : 14}]

with open("data.json", mode="w", encoding="utf_8") as write_file:
    json.dump(score, write_file, indent = 4)

with open("data.json", mode="r", encoding="utf_8") as read_file:
    python_score = json.load(read_file)

print(type(python_score))

python_score.append({"Pseudo" : "Ahoussou","Score" : 200,"Difficulté" : 14})

with open("data.json", mode="w", encoding="utf_8") as write_file:
    json.dump(python_score, write_file, indent = 4)
