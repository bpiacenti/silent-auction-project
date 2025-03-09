import art
print(art.logo)

bids = {}
continue_bidding = True

def compare_bids(bidding_dictionary):
    print(bidding_dictionary)
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder


    print(f"The winner is {winner} with a bid of ${highest_bid}")

while continue_bidding:
    name = input("What is your name?")
    price = int(input("Place your bid:\n"))

    bids[name] = price

    should_continue = input("More bidders? Y/N\n").lower()

    if should_continue == "n":
        continue_bidding = False
        compare_bids(bids)
    elif should_continue == "y":
        print("\n" * 40)