import argparse
import json
from person import person
from address import address

#Variables
outputPath = "../output/output.json"

#Arguments
parser = argparse.ArgumentParser(description = "Generates Fake information for non-existing danish persons")
parser.add_argument("--instances", type = int, default = 1, help = "How many data instances to generate, value = int")
parser.add_argument("--datatype", type = str, default = "address",
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
  if datatype == 'address':
    jsonString = '['
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
      
        





main()


