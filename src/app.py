import argparse
import json
from person import person

#Variables
outputPath = "../output/output.json"

#Arguments
parser = argparse.ArgumentParser(description = "Generates Fake information for non-existing danish persons")
parser.add_argument("--instances", type = int, default = 1, help = "How many data instances to generate, value = int")
parser.add_argument("--datatype", type = str, default = "person",
  choices=['cpr', 'namegender', 'namegenderbirthdate', 'cprnamegender', 'cprnamegenderbirthdate', 'address', 'phone', 'person'], help = "What to generate" )
args = parser.parse_args()

def main():
  instances = args.instances
  datatype = args.datatype

  if datatype == 'person':
    jsonString = '['
    for it in range (1, instances+1):
      tempPerson = person()
      tempJsonString = tempPerson.toJson()
      if it is not instances:
        tempJsonString = tempJsonString + ','
      jsonString = jsonString + tempJsonString
    jsonString = jsonString + ']'
    with open(outputPath, "w+") as file:
      file.write(jsonString)



main()



# yoperson = person()
# yoperson.printPerson()

