import pandas as pd
import csv    
import os

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

def export_txt(filename, arr):
    output_file = open(filename, 'w')
    for element in arr:
        output_file.write(str(element) + '\n')
    output_file.close()
    return   

def read_txt(filename):
    arr = []
    with open(filename) as file:
        for line in file:
            arr.append(line.rstrip())

    return arr

def main():

    if os.path.isfile('top_array.txt') and os.path.isfile('bottom_array.txt'): #if separate lists exist for 
        top_array= read_txt('top_array.txt')
        bottom_array= read_txt('bottom_array.txt')

    else:
        col_list = ["Email address", "Full Name"] #extracting only the important values (for now): email, full name
        df = pd.read_csv("form_responses.csv", usecols=col_list) #reading in the form responses exported to csv into a dataframe
        participants =df.values.tolist() #converts dataframe of form responses to list

        if len(participants) == 0:
            print("no one has signed up. Pairs are not possible at this time")
            return
        elif len(participants) == 1:
            print("only one person has signed up. Pairs are not possible at this time")
            return
        top_array, bottom_array = split_list(participants) 
        print("type:", type(top_array))
        if len(participants) % 2 != 0: #odd number of participants
            top_array.append(0) #top array will need a temporary holder of 0, the 0 will indicate that this person does not receive a pair for the week

    #initiate round robin lineup
    top_array, bottom_array = rotate(top_array, bottom_array) 

    #create the pairs for the week
    pairs_of_the_week = list(zip(top_array, bottom_array))

    #export top and bottom arrays to txt file
    export_txt('top_array.txt', top_array)
    export_txt('bottom_array.txt', bottom_array)

    return pairs_of_the_week

