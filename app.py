import argparse

parser = argparse.ArgumentParser(description = "Generates Fake information for non-existing danish persons")
parser.add_argument("--instances", type = int, default = 5, help = "How many data instances to generate, value = int")
parser.add_argument("--datatype", type = str, default = "person",
  choices=['cpr', 'namegender', 'namegenderbirthdate', 'cprnamegender', 'cprnamegenderbirthdate', 'address', 'phone', 'person'], help = "What to generate" )


