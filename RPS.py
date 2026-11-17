
def player(prev_play, opponent_history=[]):
    if prev_play == "":
        opponent_history.clear()

    opponent_history.append(prev_play)

    if len(opponent_history) <= 1:
        return "P"

    last_ten = opponent_history[-10:]
    counts = {
        "R": last_ten.count("R"),
        "P": last_ten.count("P"),
        "S": last_ten.count("S")
    }

    prediction = max(counts, key=counts.get)

    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    return counter[prediction]
