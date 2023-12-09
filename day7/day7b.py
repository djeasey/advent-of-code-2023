import pandas as pd

f = open("day7/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

df = pd.DataFrame(columns=["hand", "bid", "score"])

def type_of_hand(hand=str):
    hand_without = hand.replace("J", "")
    number_of_jacks = len(hand) - len(hand_without)
    if len(set(hand_without)) == 1 or number_of_jacks == 5:
        return "6"  # 6: Five of a kind
    elif len(set(hand_without)) == 2:
        if (
            hand_without.count(hand_without[0]) == 4 - number_of_jacks
            or hand_without.count(hand_without[1]) == 4 - number_of_jacks
        ):
            return "5"  # 5: Four of a kind
        else:
            return "4"  # 4: Full house
    elif len(set(hand_without)) == 3:
        if (
            hand_without.count(hand_without[0]) == 3 - number_of_jacks
            or hand_without.count(hand_without[1]) == 3 - number_of_jacks
            or hand_without.count(hand_without[2]) == 3 - number_of_jacks
        ):
            return "3"  # 3: Three of a kind
        else:
            return "2"  # 2: Two pair
    elif len(set(hand_without)) == 4:
        return "1"  # 1: One pair
    else:
        return "0"  # 0: Nothing


def card_to_score(card=str):
    if card == "A":
        return "12"
    elif card == "K":
        return "11"
    elif card == "Q":
        return "10"
    elif card == "J":
        return "00"
    elif card == "T":
        return "09"
    else:
        return str(int(card) - 1).zfill(2)


def score_of_hand(hand):
    # First digit is a number from 0 to 6 for the type of hand
    # Second and third digit is a number from 0 to 12 for the first card
    # Fourth and fifth digit is a number from 0 to 12 for the second card
    # etc.
    score = ""
    score = score + type_of_hand(hand)
    for card in hand:
        score = score + card_to_score(card)
    return int(score)


for line in lines:
    input = line.split()
    hand = input[0]
    bid = int(input[1])
    score = score_of_hand(hand)
    df.loc[len(df)] = {
        "hand": hand,
        "bid": bid,
        "score": score,
    }

df["rank"] = df["score"].rank(ascending=True)

df["output"] = df["bid"] * df["rank"]

print(int(sum(df["output"])))
