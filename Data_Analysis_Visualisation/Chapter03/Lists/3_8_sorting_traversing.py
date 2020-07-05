# List sorting and Traversing
seq=(41, 12, 9, 74, 3, 15)      # use sequence for creating a list
tickets = list(seq)

print(tickets)
tickets.sort()
print(tickets)

print("\nSorted list elements ")
for ticket in tickets:
    print(ticket)