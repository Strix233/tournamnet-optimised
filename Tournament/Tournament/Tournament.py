import json
#stating all arrays at begining of the program
MAX_INDIVIDUALS=20
MAX_TEAMS=4
SoloEvents = []
GroupEvents = []
Teams = []
Individuals = []
def SaveData():
    FileName = GetFileName("Enter name to save game: ")
    Data = {}
    Data["SoloEvents"]=SoloEvents
    Data["GroupEvents"]=GroupEvents
    Data["Teams"]=Teams
    Data["Individuals"]=Individuals
    with open(FileName + '.json', 'w') as f:
        json.dump(Data, f)
        print("Game saved as:", FileName)
def LoadData():
    global SoloEvents, GroupEvents, Teams, Individuals
    FileName = GetFileName("Enter save file name to load: ")
    try:
        with open(FileName + '.json', 'r') as f:
            Data = json.load(f)
            SoloEvents = Data.get("SoloEvents", [])
            GroupEvents = Data.get("GroupEvents", [])
            Teams = Data.get("Teams", [])
            Individuals = Data.get("Individuals", [])
    except FileNotFoundError:
        print("Save file not found.")
    except json.JSONDecodeError:
        print("Error reading the save file. Ensure it is a valid format.")
    print("Team Events: ", GroupEvents)
    print("SoloEvents: ", SoloEvents)
    print("Teams: ", Teams)
    print("Participants: ", Individuals)

def GetFileName(prompt):
    FileName = input(prompt)
    if FileName.strip():
        return FileName
    else:
       return None
def AddIndividuals():
    Points = 0
    for i in range(0,MAX_INDIVIDUALS):
        Name = input("Please enter the name of the participant: ")
        Individuals.append([Name, Points])

def AddTeams():
    Points = 0
    for i in range(0,MAX_TEAMS):
        TeamName = input("What is the team name? : ")
        Member1 = input("Please enter the name of the first team member: ")
        Member2 = input("Please enter the name of the second team member: ")
        Member3 = input("Please enter the name of the third team member: ")
        Member4 = input("Please enter the name of the fourth team member: ")
        Member5 = input("Please enter the name of the fifth team member: ")
        Teams.append([TeamName, Points, Member1, Member2, Member3, Member4, Member5])

def AddParticipants():
    print("First, Individuals")
    AddIndividuals()
    print("Now teams")
    AddTeams()

def AddEvents():
    #Team events
    print("First are team events")
    for i in range(0,5):
        EventName = input("Please enter the event name: ")
        GroupEvents.append(EventName)
    #Solo events
    print("Next are solo events")
    for i in range(0,5):
        EventName = input("Please enter the event name: ")
        SoloEvents.append(EventName)

def DisplayMenu():
    print("Welcome to the tournament!")
    print("In order to begin you have to add participants and events, this can be done by using options below or using the start tournament option which will guide you on how to do it!")
    print("A. Add participants")
    print("B. Add Events")
    print("C. Run Tournament")
    print("D. Start tournament (Guided option)")
def VerifyGroupInput(prompt):
    name = input(prompt)
    valid = False
    while not valid:
        for i in range(0, MAX_TEAMS):
            if Teams[i][0] == name:
                valid = True
                return name
        print("Team name invalid, please try again")
        name = input("Please try to reenter the team name: ")

            
def VerifySoloInput(prompt):
    name = input(prompt)
    valid = False
    while not valid:
        for i in range(0, MAX_INDIVIDUALS):
            if Individuals[i][0] == name:
                valid = True
                return name
        print("Name invalid, please try again")
        name = input("Please try to reenter the name: ")

def RunTeamEvents():
    Repeated=True
    while Repeated!=False:
            for i in range(0,5):
                print(GroupEvents[i], "event start")
                print("Now we have to assign placement for each team that took part in the event")
                First=VerifyGroupInput("Who got 1st place")
                Second=VerifyGroupInput("Who got 2nd place")
                Third=VerifyGroupInput("Who got 3rd place")
                Fourth=VerifyGroupInput("Who got 4th place")
                if len({First, Second, Third, Fourth}) == 4:
                    Repeated=False
                    for j in range(0,MAX_TEAMS):
                        if Teams[j][0] == First:
                            Teams[j][1] += GroupPlaceIntoPoints("First")
                        elif Teams[j][0] == Second:
                            Teams[j][1] += GroupPlaceIntoPoints("Second")
                        elif Teams[j][0] == Third:
                            Teams[j][1] += GroupPlaceIntoPoints("Third")
                        elif Teams[j][0] == Fourth:
                            Teams[j][1] += GroupPlaceIntoPoints("Fourth")
                else:
                    print("Error had to be made, team name repeated.")
    DisplayTeamScoreBoard()


def RunSoloEvents():
    Repeated=True
    while Repeated!=False:
            for i in range(0,5):
                    Repeated=True
                    print(SoloEvents[i], "event start")
                    print("Now we have to assign placement for each team that took part in the event")
                    First=VerifySoloInput("Who got 1st place")
                    Second=VerifySoloInput("Who got 2nd place")
                    Third=VerifySoloInput("Who got 3rd place")
                    Fourth=VerifySoloInput("Who got 4th place")
                    Fifth=VerifySoloInput("Who got 5th place")
                    Sixth=VerifySoloInput("Who got 6th place")
                    Seventh=VerifySoloInput("Who got 7th place")
                    Eighth=VerifySoloInput("Who got 8th place")
                    Nineth=VerifySoloInput("Who got 9th place")
                    Tenth=VerifySoloInput("Who got 10th place")
                    Eleventh=VerifySoloInput("Who got 11th place")
                    Twelveth=VerifySoloInput("Who got 12th place")
                    Thirtheenth=VerifySoloInput("Who got 13th place")
                    Fourteenth=VerifySoloInput("Who got 14th place")
                    Fifteenth=VerifySoloInput("Who got 15th place")
                    Sixteenth=VerifySoloInput("Who got 16th place")
                    Seventeenth=VerifySoloInput("Who got 17th place")
                    Eighteenth=VerifySoloInput("Who got 18th place")
                    Nineteenth=VerifySoloInput("Who got 19th place")
                    Twentyth=VerifySoloInput("Who got MAX_INDIVIDUALSth place")
                    if len({First, Second, Third, Fourth,Fifth,Sixth,Seventh,Eighth,Nineth,Tenth,Eleventh,Twelveth,Thirtheenth,Fourteenth,Fifteenth,Sixteenth,Seventeenth,Eighteenth,Nineteenth,Twentyth}) == MAX_INDIVIDUALS:
                        Repeated=False
                        for j in range(0,MAX_INDIVIDUALS):
                            if Individuals[j][0] == First:
                                Individuals[j][1] +=IndividualPlaceIntoPoints("First")
                            elif Individuals[j][0] == Second:
                                 Individuals[j][1] +=IndividualPlaceIntoPoints("Second")
                            elif Individuals[j][0] == Third:
                               Individuals[j][1] +=IndividualPlaceIntoPoints("Third")
                            elif Individuals[j][0] == Fourth:
                                Individuals[j][1] +=IndividualPlaceIntoPoints("Fourth")
                            elif Individuals[j][0] == Fifth:
                                 Individuals[j][1] +=IndividualPlaceIntoPoints("Fifth")
                            elif Individuals[j][0] == Sixth:
                               Individuals[j][1] +=IndividualPlaceIntoPoints("Sixth")
                            elif Individuals[j][0] == Seventh:
                                Individuals[j][1] +=IndividualPlaceIntoPoints("Seventh")
                            elif Individuals[j][0] == Eighth:
                                 Individuals[j][1] +=IndividualPlaceIntoPoints("Eighth")
                            elif Individuals[j][0] == Nineth:
                               Individuals[j][1] +=IndividualPlaceIntoPoints("Nineth")
                            else:
                                Individuals[j][1] +=IndividualPlaceIntoPoints("Below")

                    else:
                        print("Error had to be made, team name repeated.")
def Menu():
    while True:
        DisplayMenu()
        Choice = input("Please enter the option you want to go with: ")
        Choice = Choice.upper()
        #Ensures no incorrect input is given, prevents program crash
        if Choice in ["A", "B", "C", "D","S","L"]:
            return Choice
        else:
            print("Invalid Option")
def RunTournament():
    print("First we will go through all of the team events")#team events
    print("Now we will move onto individual events") #individual events
    RunTeamEvents()
    RunSoloEvents()
    DisplayIndividualScoreBoard()
    DisplayTeamScoreBoard()
def IndividualPlaceIntoPoints(PlaceGotten):
    if PlaceGotten=="First":
        return MAX_INDIVIDUALS
    elif PlaceGotten=="Second":
        return 15
    elif PlaceGotten=="Third":
        return 10
    elif PlaceGotten=="Fourth":
        return 8
    elif PlaceGotten=="Fifth":
        return 7
    elif PlaceGotten=="Sixth":
        return 6
    elif PlaceGotten=="Seventh":
        return 5
    elif PlaceGotten=="Eighth":
        return 4
    elif PlaceGotten=="Nineth":
        return 3
    else:
        return 2
def GroupPlaceIntoPoints(PlaceGotten):
    if PlaceGotten=="First":
        return MAX_INDIVIDUALS
    elif PlaceGotten=="Second":
        return 15
    elif PlaceGotten=="Third":
        return 10
    else:
        return 5
def Tournament():
    TournamentDone = False
    ParticipantsReady = False
    EventsReady = False
    while TournamentDone != True:
        Choice = Menu()
        if Choice == "A":
            if ParticipantsReady == False:
                print("Option chosen: Add participants")
                print("You will have to add first all individuals and then teams")
                AddParticipants()
                ParticipantsReady = True
            else:
                print("Participants are already entered")
        elif Choice == "B":
            if EventsReady == False:
                print("Option chosen: Add events")
                print("First you will add team events then solo events, they can be of any nature but will be separate")
                AddEvents()
                EventsReady = True
            else:
                print("Events are already entered")
        elif Choice == "C":
            if ParticipantsReady == True and EventsReady == True:
                RunTournament()
                TournamentDone = True
            else:
                print("Either the participants or events are not prepared")
        elif Choice == "D":
            print("Guided option chosen")
            print("First add participants")
            AddParticipants()
            print("Next, add events")
            AddEvents()
            RunTournament()
            TournamentDone = True
        elif Choice == "S":
            SaveData()
        elif Choice=="L":
            LoadData()
            EventsReady = True
            ParticipantsReady = True

def DisplayTeamScoreBoard():
    print("Displaying Team Scoreboard")
    n = len(Teams)
    for i in range(n):
        for j in range(0, n-i-1):
            if Teams[j][1] < Teams[j+1][1]:
                Teams[j], Teams[j+1] = Teams[j+1], Teams[j]
    for i in range(0,MAX_TEAMS):
        print(i+1, Teams[i][0], Teams[i][1])
def DisplayIndividualScoreBoard():
    print("Displaying individuals Scoreboard")
    n = len(Individuals)
    for i in range(n):
        for j in range(0, n-i-1):
            if Individuals[j][1] < Individuals[j+1][1]:
                Individuals[j], Individuals[j+1] = Individuals[j+1], Individuals[j]
    for i in range(0,MAX_INDIVIDUALS):
        print(i+1, Individuals[i][0], Individuals[i][1])
Tournament()