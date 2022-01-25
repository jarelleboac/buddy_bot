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

def write_csv(filename, arr):
    with open(filename, 'w', newline='') as csvfile: #should be gfg fix later
        writer = csv.writer(csvfile)
        writer.writerows(arr)
    return

def read_csv(filename):
    if filename == 'top_array.csv' or filename == 'bottom_array.csv':
        df = pd.read_csv(filename, header=None)
    else:
        df = pd.read_csv(filename, usecols=["Email address", "Full Name"])
    arr =df.values.tolist()
    return arr

def main():

    if os.path.isfile('top_array.csv') and os.path.isfile('bottom_array.csv'): #if separate lists exist for 
        try:
            top_array= read_csv('top_array.csv')
        except:
            print("yikes")
        bottom_array= read_csv('bottom_array.csv')

    else:
        participants= read_csv("form_responses.csv")

        if len(participants) == 0:
            print("no one has signed up. Pairs are not possible at this time")
            return
        elif len(participants) == 1:
            print("only one person has signed up. Pairs are not possible at this time")
            return
        top_array, bottom_array = split_list(participants) 
        if len(participants) % 2 != 0: #odd number of participants
            top_array.append(['0', '0']) #top array will need a temporary holder of 0, the 0 will indicate that this person does not receive a pair for the week

    #initiate round robin lineup
    top_array, bottom_array = rotate(top_array, bottom_array) 
    #create the pairs for the week
    pairs_of_the_week = list(zip(top_array, bottom_array))

    #export top and bottom arrays to txt file
    write_csv('top_array.csv', top_array)
    write_csv('bottom_array.csv', bottom_array)

    return pairs_of_the_week
