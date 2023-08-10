from art import logo
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print (logo)

auction_participants = {}
other_bidders = True


print("Welcome to the silent auction")
while other_bidders:                                 #put into a while loop to run as long as there are other bidders involved. Flag will change to false if "no"
  name = input("Please enter your name: ")
  bid = input("Please enter your maximum bid: $ ")
  #print(f"Parameters so far, name: {name} and bid: {bid}")   --- Test to see if inputs are working
  auction_participants[name] = bid                  #adding the name (key) and bid (value) to the dictionary (auction_participants)
  other_bidders = input("Are there other bidders? Enter 'yes' or 'no': ")
  if other_bidders == "yes":
    clear()                                         #clears the screen so the next bidder can enter their information
  else:                                             #if there are no other bidders this sets the flag to false, exits the loop and prints the highest bidder
    other_bidders = False
    #print(auction_participants)
    winner = max(auction_participants, key=auction_participants.get)             #function to grab the maximum value entry and the associated key (name)
    # variable name = max(dictionary_name, key = dictionary_name.get) gets the max Value and its Key
    # also works with "min" in place of max for the lowest bid
    
    #print(maximum, auction_participants[maximum])
    print(f"The highest bidder is {winner} with a bid of ${auction_participants[winner]}")
    