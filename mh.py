import random
import matplotlib.pyplot as plt
import numpy as np

# Monty Hall problem defintion as a class
class MH:

  # section 3.1 attributes to save MH state
    def __init__(self):
        self.n_doors = 3
        self.n_trials = 0
        self.n_sw = 0
        self.sw_w_n = 0
        self.sw_w = []
        self.st_w_n = 0
        self.st_w = []

    def getSwitchFrequency(self):
        return self.sw_w

    def getStayFrequency(self):
        return self.st_w

    # section 3.1 __str___ reporting state
    def __str__(self):
        reporting = ""
        reporting += "   n_doors = " + str(self.n_doors) + "\n"
        reporting += "   n_trials = " + str(self.n_trials) + "\n"
        reporting += "   n_sw = " + str(self.n_sw) + "\n"
        reporting += "   sw_w_n = " + str(self.sw_w_n) + "\n"
        reporting += "   sw_w  ["+str(len(self.sw_w))+"] = "
        if(len(self.sw_w) > 0):
            reporting += "["
            for d in self.sw_w:
                reporting += str(d) + ", "
            reporting += "]..."
        else:
            reporting += "[]..."
        reporting += "\n"

        reporting += "   st_w_n = "+str(self.st_w_n) + "\n"

        reporting += "   st_w  ["+str(len(self.st_w))+"] = "
        if(len(self.st_w) > 0):
            reporting += "["
            for d in self.st_w:
                reporting += str(d) + ", "
            reporting += "]..."
        else:
            reporting += "[]..."
        reporting += "\n"

        return reporting
    
    
    def trial(self):
        correct_door = self.generateWinningDoor()
        player_choice = self.generatePlayerChoice()
        is_player_switch = self.generatePlayerSwitch()
        goat_door = self.generateGoatDoor(correct_door, player_choice)
        switch_door = self.getSwitchChoiceDoor(player_choice, goat_door)
 
        print("cDoor: "+str(correct_door),end=" - ")
        print("gDoor: "+str(goat_door),end=" - ")
        print("choice: "+str(player_choice),end=" - ")
        print("switch: "+str(is_player_switch),end=" - ")
        print("sChoice: "+str(switch_door),end=" - ")
        if(correct_door == player_choice):
            print("\n**** Player choose correct door!!!")
        
        self.state_update(correct_door, goat_door, player_choice, is_player_switch, switch_door)

    def state_update(self, cdoor, gdoor, pchoice,isSwitch,sdoor):
        print("\ncorrect door: "+str(cdoor))
        print("goat door: "+str(gdoor))
        print("player choice: "+str(pchoice))
        print("do a switch: "+str(isSwitch))

        # increment trial
        self.n_trials += 1
        # increment number of switches if switch is true
        if(isSwitch): #determination to switch and calculating switch stats
            self.n_sw += 1
            # increment number of wins because of a switch
            if(sdoor == cdoor):
                self.sw_w_n += 1
#                self.sw_w.append((self.n_trials - self.n_sw) / (self.n_trials - self.n_sw))
                self.sw_w.append(1.0)
            else:
                self.sw_w.append(0.0)
            self.st_w.append(0.0)
        else:   # determination to stay and calculating stay stats
            if(cdoor == pchoice):  # player stay choice wins
                self.st_w_n += 1
#                self.st_w.append((self.n_sw) / (self.n_trials - (self.n_trials - self.n_sw)))
                self.st_w.append(1.0)
            else:   # staying resulted in not winning
                self.st_w.append(0.0)
            self.sw_w.append(0.0)





    def trial_sequence(self):
        pass

    # section 3.3 selecting door that is the alternative choice to the player
    def getSwitchChoiceDoor(self, pdoor, gdoor):
        sdoor = self.generateWinningDoor()
        while(sdoor == pdoor or sdoor == gdoor):
            sdoor = self.generateWinningDoor()
        return sdoor

    # section 3.3 selecting door with guaranteed goat
    def generateGoatDoor(self, cdoor, pdoor):
        gdoor = self.generateWinningDoor()
        while(gdoor == cdoor or gdoor == pdoor):
            gdoor = self.generateWinningDoor()
        return gdoor

    # section 3.2 select random winning door that has the car
    def generateWinningDoor(self):
        return random.randrange(3)+1
    # section 3.2 player's choice among the 3 doors
    def generatePlayerChoice(self):
        return random.randrange(3)+1
    # section 3.2 the player's choice to switch doors or not
    #   True means player switch, False means does not switch
    def generatePlayerSwitch(self):
        return bool(random.randrange(2))



if __name__ == "__main__": 
    mh1 = MH()
    for i in range(20):
        print(mh1.trial())
        print(mh1)
#    random.seed(42)
#    mh = MH()
#    print(mh)
#    mh.trial()
#    print(mh) 
#    mh.trial() 
#    print(mh) 
#    mh.trial() 
#    print(mh)

plt.plot(mh1.sw_w, "r", label="Switch")
plt.plot(mh1.st_w, "b", label="no switch")
plt.legend()
plt.title("Monty Hall Problem")
plt.xlabel("n")
plt.ylabel("prob")
plt.grid()
plt.show()