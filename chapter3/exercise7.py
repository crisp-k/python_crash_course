to_invite = ["Sarah", "John", "Steph"]
print(f"\nYou are invited: {to_invite[0]}!")
print(f"You are invited: {to_invite[1]}!")
print(f"You are invited: {to_invite[2]}!\n")

print(f"\t\t{to_invite[1]} cannot make it to the party")

new_invite = "Mista"

to_invite[1] = new_invite

print(f"\nYou are invited: {to_invite[0]}!")
print(f"You are invited: {to_invite[1]}!")
print(f"You are invited: {to_invite[2]}!\n")

print("\t\tA bigger table has been found!")

to_invite.insert(1, "Korg")
to_invite.insert(1, "Capt")
to_invite.append("Wint")

print(f"\nYou are invited: {to_invite[0]}!")
print(f"You are invited: {to_invite[1]}!")
print(f"You are invited: {to_invite[2]}!")
print(f"You are invited: {to_invite[3]}!")
print(f"You are invited: {to_invite[4]}!")
print(f"You are invited: {to_invite[5]}!\n")

print("\t\tThe table will not arrive in time, only two guests may be invited")

not_invited = to_invite.pop(1)
print(f"\nSorry {not_invited}, you are no longer invited")
not_invited = to_invite.pop(1)
print(f"Sorry {not_invited}, you are no longer invited")
not_invited = to_invite.pop(1)
print(f"Sorry {not_invited}, you are no longer invited")
not_invited = to_invite.pop(1)
print(f"Sorry {not_invited}, you are no longer invited\n")

print(f"{to_invite[0]} and {to_invite[1]}, you are both still invited\n")

del to_invite[0]
del to_invite[0]

print(to_invite)