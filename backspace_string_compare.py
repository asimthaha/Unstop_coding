bob=list(input())
alice=list(input())

i = 0
while i < len(bob):
    if bob[i] == "#":
        # Remove the character before and the '#' character itself
        if i > 0:
            bob.pop(i - 1)  # Remove the character before '#'
            i -= 1  # Adjust index because the list has shrunk
        bob.pop(i)  # Remove the '#' character
    else:
        i += 1  # Move to the next 

i=0
while i < len(alice):
    if alice[i] == "#":
        # Remove the character before and the '#' character itself
        if i > 0:
            alice.pop(i - 1)  # Remove the character before '#'
            i -= 1  # Adjust index because the list has shrunk
        alice.pop(i)  # Remove the '#' character
    else:
        i += 1  # Move to the next character

if bob == alice:
  print("YES")
else:
  print("NO")
