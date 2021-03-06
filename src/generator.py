import json
import random
import string
from secrets import choice

class Generator:
### For The Person

    #Extract Random First Name, Last Name, and Gender from the sample file
    # Input - Sample File Location
    # Output - Dictionary, ex. {'name': '?', 'surname': '?', 'gender': '?'}
    @staticmethod
    def genFullNameAndGender(sampleFile = "../datasamples/person-names.json"):
        with open(sampleFile, "r", encoding='UTF-16') as f:
            data = json.load(f)
            #Generate Random Number 
            rIndex = random.randint(0, len(data["persons"])-1)
            return data["persons"][rIndex]

    #Generates Random Birth Date
    # Input - None
    # Output - String: 'dd-MM-yyyy'
    @staticmethod
    def genBirthDate():
        day = str(random.randint(1,28))
        if len(day) < 2:
            day = f'0{day}'
        month = str(random.randint(1,12))
        if len(month) < 2:
            month = f'0{month}'
        year = str(random.randint(1930,2020))
        return f'{day}-{month}-{year}'

    #Generate Last 4 digits of a CPR
    # Input - gender 'male' or 'female', birthday of dd-mm-yyyy format
    # Output - String: birthday without '-' + random 4 digit number, even for females, odd for males 
    @staticmethod
    def genCPR(gender, birthday):
        #Formatting the birthday:
        formattedBirthday = birthday.replace('-', '')
        formattedBirthday = formattedBirthday[:4] + formattedBirthday[6:8]
        #Generating the first 3 of the last 4 numbers:
        firstThree = str(random.randint(100,999))
        #Generating the last number:
        if gender == 'male':
            options = [1,3,5,7,9]
            lastOne = str(random.choice(options))
        if gender == 'female':
            options = [2,4,6,8]
            lastOne = str(random.choice(options))
        return f'{formattedBirthday}-{firstThree}{lastOne}'

# For The Address

    #Extracts random street name from the provided sample file
    # Input - sample file location
    # Output - String: address, ex: 'Leensgade'
    @staticmethod
    def genStreet(sampleFile = "../datasamples/street-names.json"):
        with open(sampleFile, "r") as f:
            data = json.load(f)
            #Generate Random Number 
            rIndex = random.randint(0, len(data["addresses"])-1)
            return data["addresses"][rIndex]['name']

    #Generates Random street number
    # Input - None
    # Output - String: Random number up to 3 digits, ocasionally with a uppercase Letter at the end 
    @staticmethod
    def genStreetNumber():
        firstPart = str(random.randint(1,999))
        optionalTrigger = random.choice(['true','false'])
        return (
            firstPart + str(random.choice(string.ascii_letters).upper())
            if optionalTrigger == 'true'
            else firstPart
        )

    #Generate Random floor number
    # Input - None
    # Output - String: number from '1'-'99' or 'st' 
    @staticmethod
    def genFloor():
        floor = random.randint(0,99)
        floor = 'st' if floor == 0 else str(floor)
        return floor

    #Generate random door number
    # Input - None
    # Output - String: 'th' or 'mf' or 'tv' followed by a number (ex. 'tv21') or a lowercase ketter optionally
    #                    followed by a dash, then by a number from 1 to 50 (ex. c3, t20, l-40)
    @staticmethod
    def genDoorNumber():
        #Either th,mf,tv followed by a number or normal address
        option1 = random.randint(1,4)
        if option1 < 2:
            letters = random.choice(['th','mf','tv'])
            number = str(random.randint(1,50))
            return letters + number
        else:
            letter = str(random.choice(string.ascii_letters).lower())
            dash = random.choice(['','-'])
            number = str(random.randint(1,50))
            return letter + dash + number

    
    #Extract Random Town and Postcode from the sample file
    # Input - Sample File Location
    # Output - Dictionary: ex. {'name': '?', 'code': '?'}
    @staticmethod
    def genTownAndPostalCode(sampleFile = "../datasamples/addresses.json"):
         with open(sampleFile, "r") as f:
            data = json.load(f)
            #Generate Random Number, 
            rIndex = random.randint(0, len(data["addresses"])-1)
            return data["addresses"][rIndex]

    #Generate Random 8 digit phone number starting with the provided options
    # Input - None
    # Output - String: Eight didit phone number (ex: '51204433')
    @staticmethod
    def genPhoneNumber():
        startingOptions = [2, 30, 31, 40, 41, 42, 50, 51, 52, 53, 60, 61, 71, 81,
                            91, 92, 93, 342, 344, 345, 346, 347, 348, 349, 356, 357,
                            359, 362, 365, 366, 389, 398, 431, 441, 462, 466, 468,
                            472, 474, 476, 478, 485, 486, 488, 489, 493, 494, 495, 496, 498, 
                            499, 542, 543, 545, 551, 552, 556, 571, 572, 573, 574, 577, 579, 584, 586, 587,
                            589, 597, 598, 627, 629, 641, 649, 658, 662, 663, 664, 665, 667, 
                            692, 663, 694, 697, 771, 772, 782, 783, 785, 786, 788, 789, 826, 827,829]
        firstPart = str(random.choice(startingOptions))
        if len(firstPart) == 1:
            phoneNumber = firstPart + str(random.randint(1000000, 9999999))
        if len(firstPart) == 2:
            phoneNumber = firstPart + str(random.randint(100000, 999999))
        else:
            phoneNumber = firstPart + str(random.randint(10000, 99999))
        return phoneNumber


# DEBUG
# print(Generator.genBirthDate())
# print(Generator.genCPR('female'))
# print(Generator.genStreet())
# print(Generator.genStreetNumber())
# print(Generator.genFloor())
# print(Generator.genDoorNumber())
# print(Generator.genTownAndPostalCode())
# print(Generator.genPhoneNumber())




    





 
            



