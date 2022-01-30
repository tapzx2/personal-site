#!/usr/local/bin/python3
import argparse


print('it works')

# parse given command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('directory', type=str,
                    help="this is the directory that holds the blurbs")
args = parser.parse_args()

print(args)

# get real path of argument
which


# for
