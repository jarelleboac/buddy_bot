import pandas as pd
import random as rd
import csv
from itertools import combinations
import smtplib
from email.message import EmailMessage
import os.path 
from os import path 
import math

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def rotate(top_array, bottom_array):
    # remove last element from top array and append to bottom array
    bottom_array.insert(len(bottom_array), top_array[len(top_array)-1])
    top_array.remove(top_array[len(top_array)-1])

    # remove the first element from bottom array and append to index 1 of top array
    top_array.insert(1, bottom_array[0])    
    bottom_array.remove(top_array[1])
    return top_array, bottom_array

def main():
    col_list = ["Email address", "Full Name"] #extracting only the important values (for now): email, full name
    df = pd.read_csv("form_responses.csv", usecols=col_list) #reading in the form responses exported to csv into a dataframe
    participants =df.values.tolist() #converts dataframe of form responses to list
    current_week_pairs = list() #list to store this week's pairs in

    if path.exists('updated_pair_combinations.csv'):
        print("it exists!")
    else:
        if len(participants) == 0:
            print("no one has signed up. Pairs are not possible at this time")
            return
        elif len(participants) == 1:
            print("only one person has signed up. Pairs are not possible at this time")
            return
        elif len(participants) % 2 == 0: #even number of participants
            print("even number of participants")

        else: #odd number of participants
            #partition participants into two lists            
            top_array, bottom_array = split_list(participants) 
            top_array.append(0) #top array will need a temporary holder of 0, the 0 will indicate that this person does not receive a pair for the week
            top_array, bottom_array = rotate(top_array, bottom_array)


if __name__ == "__main__":
    main()
