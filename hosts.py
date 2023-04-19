#!/bin/env python3

import argparse
import sys
import time

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

parser = argparse.ArgumentParser(description='Processing hosts files based on various different arguments')


parser.add_argument("-a", "--all", action="store_true")
parser.add_argument("-d", "--domain", action="store")
parser.add_argument("-c", "--classes", action="store")
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
    domain = args.domain
    count = 0
    # print(args.domain)
    for eachLine in result:
        if domain in eachLine:
            count += 1
            print(eachLine)
        else:
            continue
    if count == 0:
        print("No hosts in the given domain")
        exit(1)
    else:
        print("Total hosts: " + str(count))

elif(args.classes):
    count = 0
    check_class = args.classes
    min_range = -sys.maxsize
    max_range = sys.maxsize
    if check_class == 'A':
        # print("Class A")
        min_range = 0
        max_range = 127
    elif(check_class == 'B'):
        # print("Class B")
        min_range = 128
        max_range = 191
    elif(check_class == 'C'):
        # print("Class C")
        min_range = 192
        max_range = 255
    else:
        print("invalid class")
        exit(1)
    for eachResult in split_result:
        ip_result = int(eachResult[0].split('.')[0])
        # print(ip_result)
        for i in range(min_range,max_range+1):
            # print(f'Checking {i} against {ip_result}')
            if i == (ip_result):
                count += 1
                # print(count)
                # print(ip_result)
                print(result[split_result.index(eachResult)])
            else:
                continue
        if count == 0:
            print("No hosts in the given class")

elif(args.version):
    first_name = "Sidak"
    last_name = "Aulakh"
    student_id = "24870952"
    date_of_completion = time.localtime()
    print(f"Name: {first_name} {last_name}")
    print(f"Student ID: {student_id}")
    print(f"Date of completion: {date_of_completion.tm_mday}/{date_of_completion.tm_mon}/{date_of_completion.tm_year}")
else:
    print("No arguments")



