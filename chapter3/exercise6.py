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
