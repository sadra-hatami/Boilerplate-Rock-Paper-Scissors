
def counter(move):
    return {"R": "P", "P": "S", "S": "R"}[move]


def predict_quincy(my_history):
    choices = ["R", "R", "P", "P", "S"]
    return [
        choices[(i + 1) % 5]
        for i in range(len(my_history) + 1)
    ]


def predict_kris(my_history):
    return [
        counter("R" if i == 0 else my_history[i - 1])
        for i in range(len(my_history) + 1)
    ]


def predict_mrugesh(my_history):
    history = []
    predictions = []

    for i in range(len(my_history) + 1):
        previous = "" if i == 0 else my_history[i - 1]
        history.append(previous)

        last_ten = history[-10:]
        most_frequent = max(
            set(last_ten), key=last_ten.count
        )

        if most_frequent == "":
            most_frequent = "S"

        predictions.append(counter(most_frequent))

    return predictions


def predict_abbey(my_history):
    history = []
    play_order = {
        a + b: 0
        for a in "RPS"
        for b in "RPS"
    }

    predictions = []

    for i in range(len(my_history) + 1):
        previous = "" if i == 0 else my_history[i - 1]

        if not previous:
            previous = "R"

        history.append(previous)

        last_two = "".join(history[-2:])

        if len(last_two) == 2:
            play_order[last_two] += 1

        potential_plays = [
            previous + "R",
            previous + "P",
            previous + "S"
        ]

        sub_order = {
            key: play_order[key]
            for key in potential_plays
        }

        prediction = max(
            sub_order, key=sub_order.get
        )[-1:]

        predictions.append(counter(prediction))

    return predictions


def player(prev_play, opponent_history=[], my_history=[]):

    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
    else:
        opponent_history.append(prev_play)

    models = [
        predict_quincy,
        predict_abbey,
        predict_kris,
        predict_mrugesh
    ]

    candidates = []

    for model in models:
        predictions = model(my_history)

        if predictions[:len(opponent_history)] == opponent_history:
            candidates.append(predictions[len(opponent_history)])

    counts = {
        move: candidates.count(move)
        for move in "RPS"
    }

    winning_scores = {
        "R": counts["S"],
        "P": counts["R"],
        "S": counts["P"]
    }

    best_move = max(
        "RPS",
        key=lambda move: winning_scores[move]
    )

    my_history.append(best_move)

    return best_move
