import argparse
import json
from random import random
from person import person
from address import address
from generator import Generator

#Variables
outputPath = "../output/output.json"

#Arguments
parser = argparse.ArgumentParser(description = "Generates Fake information for non-existing danish persons")
parser.add_argument("--instances", type = int, default = 1, help = "How many data instances to generate, value = int")
parser.add_argument("--datatype", type = str, default = "person",
  choices=['cpr', 'namegender', 'namegenderbirthdate', 'cprnamegender', 'cprnamegenderbirthdate', 'address', 'phone', 'person'], help = "What to generate" )
args = parser.parse_args()

#TODO
#Bring proper structure to main
def main():
  instances = args.instances
  datatype = args.datatype

  if datatype == 'person':
    #TODO
    #Extract Method
    #Test Method
    jsonString = '['
    for it in range (1, instances+1):
      tempPerson = person()
      tempJsonString = tempPerson.toJson()
      if it is not instances:
        tempJsonString = tempJsonString + ','
      jsonString += tempJsonString
    jsonString += ']'
    with open(outputPath, "w+") as file:
      file.write(jsonString)

  #TODO
  #Extract Method
  #Test Method
  if datatype == 'address':
    jsonString = '[ {'
    for it in range (1, instances+1):
      tempAddress = address()
      tempJsonString = str(tempAddress.__dict__).replace('{','')
      tempJsonString = tempJsonString.replace("'",'"')
      if it is not instances:
        tempJsonString = tempJsonString + ','
      jsonString += tempJsonString
    jsonString += ']'
    with open(outputPath, "w+") as file:
      file.write(jsonString)

  #TODO
  #Extract Method
  #Test Method
  if datatype == 'birthday':
    jsonString = '['
    for it in range (1, instances+1):
      tempBirthday = Generator.genBirthDate()
      genderOptions = ['male','female']
      tempGender = random.choice(genderOptions)
      tempCPR = Generator.genCPR(tempGender, tempBirthday)
      tempJsonString = '{"cpr":'
      tempJsonString += f'"{tempCPR}"'
      tempJsonString += '}'
      if it is not instances:
        tempJsonString += ','
      jsonString += tempJsonString
      jsonString += ']'
    with open(outputPath, "w+") as file:
      file.write(jsonString)



      
        





main()


