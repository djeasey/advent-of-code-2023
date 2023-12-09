import pandas as pd

f = open("day7/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

df = pd.DataFrame(columns=["hand", "bid", "score"])

def type_of_hand(hand=str):
    if len(set(hand)) == 1:
        return "6"  # 6: Five of a kind
    elif len(set(hand)) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            return "5"  # 5: Four of a kind
        else:
            return "4"  # 4: Full house
    elif len(set(hand)) == 3:
        if (
            hand.count(hand[0]) == 3
            or hand.count(hand[1]) == 3
            or hand.count(hand[2]) == 3
        ):
            return "3"  # 3: Three of a kind
        else:
            return "2"  # 2: Two pair
    elif len(set(hand)) == 4:
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
        return "09"
    elif card == "T":
        return "08"
    else:
        return str(int(card) - 2).zfill(2)


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
