p1 = input("\nPlayer 1, make your move (case insensitive): ")
p1 = p1.lower()
# Convert user input in any case into lowercase so that if user enters an input containing uppercase letter(s) like
# "ROCK", "Rock", "RoCk", "roCK", etc, we can render all of them as the lowercase ones, which, in this example,
# is "rock".
if p1 == "rock" or p1 == "paper" or p1 == "scissors":
    p2 = input("\nPlayer 2, make your move (case insensitive): ")
    p2 = p2.lower()
    if p2 == "rock" or p2 == "paper" or p2 == "scissors":

        if p1 == p2:                             # The scenarios that would lead to the 1st class of results (Draw).
            print("\nDraw/Tie!\n")

        elif p1 == "rock" and p2 == "scissors":  # The scenarios that would lead to the 2nd classes of results (P1 wins)
            print("\np1 wins\n")
        elif p1 == "paper" and p2 == "rock":
            print("\np1 wins\n")
        elif p1 == "scissors" and p2 == "paper":
            print("\np1 wins\n")

        else:                                    # The scenarios that would lead to the 3nd classes of results (P2 wins)
            print("\np2 wins\n")

    else:
        print("\nInvalid move. Only \"rock\", \"paper\" and \"scissors\" (case insensitive) are valid. "
              "Other inputs (including empty input) is invalid.\n")
else:
    print("\nInvalid move. Only \"rock\", \"paper\" and \"scissors\" (case insensitive) are valid. "
          "Other inputs (including empty input) is invalid.\n")
