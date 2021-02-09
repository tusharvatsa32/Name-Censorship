"""
S21 11-411 NLP Assignment 1 Part 1
Name-Censoring Cleaner Class
Sabyasachi Mohanty - 4 February 2021

Cleaner class implements a method clean that, given a list of
censored full names, censored last names, and an input string,
removes the censored full names and last names from the input
and replaces it with a 'politically correct' name.

USAGE: python cleaner.py BANNED_NAMES_FILE INPUT_FILE
BANNED_NAMES_FILE - .txt file containing a list of banned names
INPUT_FILE - .txt file containing the original article

No input validation is performed

Provides an executable script for running implemented class
on a specific file

"""

import re
import sys


class BaseCleaner():
    """
    Abstract class for the text censoring object
    """

    def __init__(self, replacement_full_name, replacement_last_name):
        """
        Initializes Cleaner object
        :param replacement_full_name: full name to replace with
        :param replacement_last_name: last name to replace with
        """
        self.replacement_full_name = replacement_full_name
        self.replacement_first_name = replacement_full_name.split()[0]
        self.replacement_last_name = replacement_last_name

    def clean(self, full_names, last_names, input_text):
        """
        Abstract method, called to censor (replace) text

        :param full_names: a list of full names to replace
        :param last_names: a list of last names to replace
        :param input_text: text string to process
        :return: processed text string
        """
        raise NotImplementedError


class Cleaner(BaseCleaner):
    """
    Student submission for text censoring object
    """

    def clean(self, full_names, last_names, input_text):
        """
        Method called to clean input text of censored full names and last names.
        Can assume that list of last names is the set of unique last names derived
        from the list of full names i.e. last_names = list(set([s.split()[-1] for s in full_names]))

        :param full_names: list of censored full names to be replaced
        :param last_names: list of censored last names to be replaced
        :param input_text: input text to process
        :return: output text with censored full names and last names removed
        """
        # TODO: IMPLEMENT
        # NOTE: Get the replacement name using self.replacement_full_name,
        #       self.replacement_first_name and self.replacement_last_name
        last_names=list([n.split()[-1] for n in full_names])
        first_names=list([n.split()[0] for n in full_names])
        print(first_names[last_names.index('Woods')])
        replacement_first_name='John'
        replacement_last_name='Smith'
        for name in range(len(first_names)):
            pattern1=re.compile(r'{fname}(?=[ ]{lname})'.format(fname=first_names[name],lname=last_names[name]))
            pattern2=re.compile(r'(?<={fname}[ ]){lname}'.format(fname=replacement_first_name,lname=last_names[name]))
            pattern3=re.compile(r'(?<!-){lname}'.format(lname=last_names[name]))

            m1=re.search(pattern1,input_text)
            m2=re.search(pattern2,input_text)
            m3=re.search(pattern3,input_text)

            if m1:
                output_str=re.sub(pattern1,replacement_first_name,input_text)
            if m2:
                output_str=re.sub(pattern2,replacement_last_name,output_str)
            if m3:
                output_str=re.sub(pattern3,replacement_last_name,output_str)
        return output_str
        


# Main executable script provided for your convenience
# Not executed on autograder, so do what you want
if __name__ == "__main__":

    # Ensure exactly two arguments
    if len(sys.argv) != 3:
        print("Usage: python cleaner.py BANNED_NAMES_FILE INPUT_FILE")
        sys.exit(1)

    BANNED_NAMES_FILE = sys.argv[1]
    INPUT_FILE = sys.argv[2]

    # Check input file type
    if not (BANNED_NAMES_FILE.endswith(".txt") and INPUT_FILE.endswith(".txt")):
        print("Error: BANNED_NAMES_FILE and INPUT_FILE must be .txt files")
        sys.exit(1)

    # Initialize new Cleaner
    cleaner = Cleaner("John Smith", "Smith")

    # Read banned names
    banned_full_names = set()
    with open(BANNED_NAMES_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                banned_full_names.add(line)
    banned_full_names = list(banned_full_names)
    # banned_last_names = list(set([n.split()[-1] for n in banned_full_names]))
    banned_last_names=list([n.split()[-1] for n in banned_full_names])
    banned_first_names=list([n.split()[0] for n in banned_full_names])
    
    # Read input
    input_contents = ""
    with open(INPUT_FILE, "r") as f:
        input_contents = f.read()
    if not input_contents:
        print("Error: Input file is empty!")
        sys.exit(1)

    # Process and print output
    print(cleaner.clean(banned_full_names, banned_last_names, input_contents))





