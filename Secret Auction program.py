from art import logo
print(logo)
Secret_Auction={}
Secret_Auction=False #Sets the value if secret auction as none
Name=[]
bids={}
def find_highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
     bid_amount=bidding_record[bidder]
     if bid_amount>highest_bid:
        highest_bid=bid_amount ##Highest bid will be the highest bid_amount pitched
        winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not Secret_Auction:
    Name=input("What is the Name of the bidder?\n")
    Bid_Price=int(input("What is the Bid Price? $\n"))
    bids[Name]=Bid_Price
    should_continue=input("Are there any other Bidders? Type 'Yes' or 'No'\n")
    if should_continue== "No":
        Secret_Auction=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
       clear()
              
