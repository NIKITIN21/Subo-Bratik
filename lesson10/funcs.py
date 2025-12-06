import data

quest_index = 0
quests_data = data.questions

def generate_quest(QUEST, buttons):
    if quest_index < len(quests_data):
        quest = quests_data[quest_index]["quest"]
        QUEST.config(text=quest)
    else:
        QUEST.config(text="Викторина закончена!")
        for btn in buttons:
            btn.config(state="disabled")
    for i in range(len(buttons)):
        buttons[i].config(text=quests_data[quest_index]["answers"][i])
def choice(button, QUEST, buttons, info):
    global quest_index
    if button["text"] == quests_data[quest_index]["right"]:
        quest_index += 1
        info.config(text="")
        generate_quest(QUEST, buttons)
    else:
        info.config(text="Ответ неверный")