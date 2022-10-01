import random

# could make this mulitmentional by giving all elements a rank based on user preference  

Museums = ["Metropolitan Museum of Art", "Natural History Museum", "Whitney Museum"]
Restaurant = ["Pizza Place @ Times Square", "Sushi Place @ 5th Ave", "Spicy joint @ 10th Ave"]

randomMuseum = random.randint(0, len(Museums)-1)
randomRest = random.randint(0, len(Restaurant)-1)
        

print("Our suggestion for a fun time is the museum [", Museums[randomMuseum], "] and our special Restaurant is ", Restaurant[randomRest])
    
#suits.append("Cooper")
#print("Adding Cooper to our suits")
#print("suits length", len(suits), " ranks lenghth ", len(ranks))

#As the user to add their favorite museum

def getUserFavoriteMuseums():
    mfromuser = input("What is your favorite museum? ")
    print("We have ", len(Museums), " in our list now.")
    Museums.append(mfromuser)
    print("We have ", len(Museums), " in our list now.")

# Restaurant = Museums


def pickRandomHotspots():
    randomMuseum = random.randint(0, len(Museums)-1)
    print("Our random Museum", Museums[randomMuseum], " and our resturant is ", Restaurant[randomRest])


getUserFavoriteMuseums() # call this function


    
