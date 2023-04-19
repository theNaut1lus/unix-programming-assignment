#!/bin/env python3

import argparse

def check_file(hosts_file):
    try:
        with open(hosts_file, 'r') as open_file:
            # print("File found")
            split_result = []
            result=[]
            for x in open_file.readlines():
                result.append(x)
                split_result.append(x.split(' '))
            open_file.close()
            return result, split_result
    except FileNotFoundError:
        print("File not found")
        exit(1)

parser = argparse.ArgumentParser(description='Processing hosts files')


parser.add_argument("-a", "--all", action="store_true")
parser.add_argument("-d", "--domain", action="store")
parser.add_argument("-c", "--classes", action="store_true")
parser.add_argument("-v", "--version", action="store_true")
parser.add_argument("file", action="store")

args = parser.parse_args()

# print(args)

result,split_result = check_file(args.file)

# print(result)
# print(split_result)

if(args.all):
    # print(result)
    if result == []:
        print("No hosts")
    else:
        print("Hostnames:")
        for eachResult in split_result: # type: ignore
            print(eachResult[1])

elif(args.domain):
    # print(args.domain)
    for eachLine in result:
        if args.domain in eachLine:
            print(eachLine)
        else:
            continue

elif(args.classes):
    print("Class")
elif(args.version):
    print("Version")
else:
    print("No arguments")



