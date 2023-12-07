import random

out_types = [
  "He's gone! Caught behind by the wicket-keeper!",
  "Bowled him! That's a peach of a delivery!",
  "Out! Leg before wicket! That's plumb!",
  "Stumped! He's out of his crease!",
  "Hit wicket! He's hit his own stumps!",
  "Run out! He's been run out by a direct hit!",
  "Timed out! He took too long to get ready to face the next ball!",
  "Handled the ball! He's given out for handling the ball!",
  "Obstructing the field! He's given out for obstructing the field!",
  "Retired out! He's retired out of the innings!",
]


tot_overs = int(input("How many overs you would like to play:"))
print("Which play you would like to play:\n"
      "1-International\n"
      "2-Indian\n")
play = input().lower()
if play == "international":
    print("Afghanistan--Australia--Bangladesh--England-India--Ireland\nNew Zealand--Pakistan--South Africa "
          "Sri Lanka--West Indies--Zimbabwe")
    u_team=input("Select your team:")
    com_team=input("Select computer team:")

else:
    print("Chennai Super Kings (CSK)             Delhi Capitals (DC)\n"
          "Kings XI Punjab (KXIP)                Kolkata Knight Riders (KKR)\n"
          "Mumbai Indians (MI)                   Rajasthan Royals (RR)\n"
          "Royal Challengers Bangalore (RCB)     Sunrisers Hyderabad (SRH)\n")
    u_team = input("Select your team:")
    com_team = input("Select computer team:")

# Toss
print("\nToday's match is : ",play)
print("Clash is between :")
print(u_team,"vs",com_team)
print("\nHere comes the Toss")
toss = (input("Choose heads or tails: ")).lower()

random_toss = random.randint(1, 2)
random_opt = random.randint(1, 2)

u_opt = 0
c_opt = 0

if random_toss == 1 and toss == "heads":
    print("\n",u_team," won the toss")
    u_opt = (input(" Choose bat or ball: ")).lower()

elif random_toss == 2 and toss == "tails":
    print("\n",u_team," won the toss")
    u_opt = (input("Choose bat or ball: ")).lower()

else:
    print("\n",u_team," lost the toss")

    if random_opt == 1:
        c_opt = "bat"
        print(com_team," choose to", c_opt)

    elif random_opt == 2:
        c_opt = "ball"
        print(com_team," choose to", c_opt)


print("\n---------- First Innings Begins ----------")

runs_1 = 0
wickets_1 = 0
balls_1 = 0
overs_1 = 0
while wickets_1 != 10 and (6*tot_overs - (overs_1 * 6 + balls_1)) > 0:

    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1, 6)

    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")

    else:
        print("",u_team,":", u_choice, "\n",com_team,":", c_choice)

        if u_choice == c_choice:
            print(random.choice(out_types))
            wickets_1 += 1

        else:
            if u_opt == "bat" or c_opt == "ball":
                Bat_first = "You"
                Ball_first = "Computer"
                runs_1 += u_choice

            elif u_opt == "ball" or c_opt == "bat":
                Bat_first = "Computer"
                Ball_first = "You"
                runs_1 += c_choice

        print("\nScore =", runs_1, "/", wickets_1)

        balls_1 += 1
        if balls_1 == 6:
            overs_1 += 1
            print("End of Over", overs_1)
            balls_1 = 0

        print("\nBalls remaining: ", 6*tot_overs - (overs_1 * 6 + balls_1))

print("\n---------- End of Innings ----------")

print("\nFinal Score:")
print("Runs =", runs_1)
print("wickets =", wickets_1)

print("\n", com_team, "needs", runs_1 + 1, "runs to win.")

print("\n---------- Second Innings Begins ----------")

runs_2 = 0
wickets_2 = 0
balls_2 = 0
overs_2 = 0
while wickets_2 != 10 and (6*tot_overs - (overs_2 * 6 + balls_2)) > 0 and runs_2 <= runs_1:

    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1, 6)

    if u_choice < 1 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")

    else:
        print(u_team,": ", u_choice, "\n",com_team,": ", c_choice)

        if u_choice == c_choice:
            print(random.choice(out_types))
            wickets_2 += 1

        else:
            if Bat_first == "Computer":
                runs_2 += u_choice
                Bat_second = "You"

            elif Bat_first == "You":
                runs_2 += c_choice
                Bat_second = "Computer"

        print("\nScore =", runs_2, "/", wickets_2)
        balls_2 += 1
        if balls_2 == 6:
            overs_2 += 1
            print("End of Over", overs_2)
            balls_2 = 0

        print("\nBalls remaining: ", 6*tot_overs - (overs_2 * 6 + balls_2))

        if runs_2 <= runs_1 and balls_2 <= ((tot_overs*6)-1) and wickets_2 != 10:
            print("To win:", runs_1 - runs_2 + 1, "runs needed from", 6*tot_overs - (overs_2 * 6 + balls_2), "balls.")

print("\n---------- End of Innings ----------")

print("\nFinal Score:")
print("Runs =", runs_2)
print("wickets =", wickets_2)

print("\n~~~~~~~~~~ Result ~~~~~~~~~~")

if runs_1 > runs_2:

    if Bat_first == "You":
        print("\nCongratulations! ",u_team," won the Match by", runs_1 - runs_2, "runs.")

    else:
        print("\nBetter luck next time! The ",com_team," won the Match by", runs_1 - runs_2, "runs.")

elif runs_2 > runs_1:

    if Bat_second == "You":
        print("\nCongratulations! ",u_team," won the Match by", 10 - wickets_2, "wickets.")

    else:
        print("\nBetter luck next time! The ",com_team," won the Match by", 10 - wickets_2, "wickets.")

else:
    print("The Match is a Tie.", "\nNo one Wins.")
