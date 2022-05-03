from replit import clear
from artist import logo
print(logo)

bids = {}
bid_goin=False
def high_bid(bids_value):
    ha=0
    for bidder in bids_value:
        amount=bids_value[bidder]
        if(amount>ha):
            ha=amount
            winner=bidder
    print(f"winner is {winner} with highest bid of rs{amount}")
        
        
        
while not bid_goin:
    name=input("Enter your name:\n")
    bid=int(input("Enter your bid in rs/-: \n"))
    bids[name]=bid
    end=input("Types yes if more bid , no if no more bids").lower()
    if(end == "no"):
        bid_goin=True
        high_bid(bids)
    elif(end == "yes"):
        clear()
    else:
        print("choose correct choice")
        end=input("Types yes if more bid , no if no more bids").lower()
