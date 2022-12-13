# Globals values
a = "*"


print(f"{a * 8} ROCK, PAPER OR SCISSORS {a * 8}")
user_option = input("\nEnter a option (rock, paper or scissor?): \n").lower()
print(user_option)

compu_option = "scissor"

if user_option == compu_option:
  print(f"{user_option} vs {compu_option} = \"Empate\"")

elif user_option == "rock":
  if compu_option == "paper":
    print(f"{user_option} vs {compu_option} = \"Computer Win\"")
  else:
    print(f"{user_option} vs {compu_option} = \"User Win\"")

elif user_option == "paper":
  if compu_option == "rock":
    print(f"{user_option} vs {compu_option} = \"User Win\"")
  else:
    print(f"{user_option} vs {compu_option} = \"Computer Win\"")

else:
  if compu_option == "rock":
    print(f"{user_option} vs {compu_option} = \"Computer Win\"")
  else:
    print(f"{user_option} vs {compu_option} = \"User Win\"")