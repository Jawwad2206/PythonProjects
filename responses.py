import random
import ts

def get_response(message:str) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Good day, how can I help you today ご主人様/ お嬢様?"

    if message == "!roll":
        return str(random.randint(1,6))

    if p_message == "!help":
        return "`ご主人様/お嬢様 I can do the following task\n " \
               "!exam -> Tells you the date for the exams\n " \
               "!ts -> Tells you when the next Tutorial Session is\n " \
               "!role -> A dice" \
               "!rules -> Will remind you again about the rules for this class`"


    if p_message == "!exam":
        return "The exam will be held on the 28.07.2023 or 11.10.2023 (WS 2023/24) until then I will help you as much as possible"

    if p_message == "!ts":

        return "The next Session will be: ", ts.wednesday().strftime("%d-%m-%Y"), "Group 14 starts 10:15 || Group 15 starts 12:00"

    return
