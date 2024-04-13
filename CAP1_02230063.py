# Name: Dorji Wangdi
# Section: 1EE
# Student ID Number: 02230063
################################
# REFERENCES
# https://www.youtube.com/watch?v=rZLvWjlT-k4&t=411s
# https://www.youtube.com/watch?v=R1TO73IhRsI
# https://www.youtube.com/watch?v=cCsEkHhHxYw&t=28s
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://github.com/golergka/advent-of-code-2022-with-chat-gpt/blob/master/day_2/version_1.py
# https://github.com/golergka/advent-of-code-2022-with-chat-gpt/blob/master/day_2/version_12.py
# https://www.reddit.com/r/PowerShell/comments/zafhdo/advent_of_code_2022_day_2_rock_paper_scissors/
################################
# SOLUTION 
# Solution Score: 49483
################################
# overall complexicity;
# Time Complexity: O(n)
# Space Complexity: O(n)
################################

# Complexity for read_input
# Time Complexity: O(n)
# Space Complexity: O(n)

# This is the function which is used to read the input file given i.e input_3_cap1.txt
def read_input(input_3_cap1):
    result = [] # empty list to store the result(rounds) data

    with open(input_3_cap1, 'r') as f: # Open the file and read each line
        for line in f: 
             result.append(line.strip().split())  # removes Strip (whitespace) and split the line, then add the list
    return result 

# Complexity for calculate_score
# Time Complexity: O(n)
# Space Complexity: O(1)

 # Function to calculate the score based on the game rules given in the assignment
def calculate_score(rounds):

    # this dictionary will show the logic behind the rock-paper-scissor
    # this are the outcomes of condition based on the given question 
    score_sum  = { 
    ('A', 'Y'): 4, ('B', 'Y'): 5, ('C', 'Y'): 6,
    ('A', 'X'): 3, ('B', 'X'): 1, ('C', 'X'): 2,
    ('A', 'Z'): 8, ('B', 'Z'): 9, ('C', 'Z'): 7
    }
    
    # the variable 'total score' will show the total sum and initially it is initializing as 0
    total_score = 0

    # Iteration over each round and will calculate the total score 
    for i in rounds:
        round_key = tuple(i) # converts the round to a tuple to use as a key in the score_sum dictionary
        # if not used typeError(unhashable type), will come 
        total_score += score_sum [round_key] # add the score for the round to the total_score

    return total_score
# This is the main execution block in the code 
if __name__ == "__main__":
    test1 = "input_3_cap1.txt" # this variable name contains the 'def calculate_score(rounds)' data   

# calling the function def
# Reading the input from the file
rounds = read_input('input_3_cap1.txt') 

# Calculating the total score
score = calculate_score(rounds)

# Print the total score
print(f"The total score is: {score}")