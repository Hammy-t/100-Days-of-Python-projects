bids = {}
loop = "yes"

while loop == "yes":
    key = input("Enter your name: ")
    value = int(input("What's your bid? $"))
    bids[key] = value
    
    loop = input("Are there any other bidders? Yes or No: ").lower()
    
    while (loop != "yes") and (loop != "no"):
        loop = input("Kindly enter a Yes or a No: ").lower()

    print("\n" * 1000)  # Clears screen (not necessary for all environments)

# Find the highest bid
highestBid = 0
highestBidder = ""

for key in bids:
    if bids[key] > highestBid:
        highestBid = bids[key]
        highestBidder = key

print(highestBidder, "has the highest bid with a bid of $", highestBid)
