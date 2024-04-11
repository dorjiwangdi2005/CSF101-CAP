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
# Your Solution Score: 49548
################################

# This is the function which is used to read the input file given i.e input_3_cap1.txt
# Time Complexity: O(n)
# Space Complexity: O(n)

def read_input(input_3_cap1):
    result = [] # empty list to store the result 

    with open(input_3_cap1, 'r') as f:
        for line in f: 
             result.append(line.strip().split())  # Strip and split the line, then add to the list
    return result 

# Function to calculate the score based on the game rules given in the assignment 
# Time Complexity: O(n)
# Space Complexity: O(1)

def calculate_score(rounds):
    scores = {'A': 1, 'B': 2, 'C': 3,'X': 0, 'Y': 3, 'Z': 6} 
    # writing a dict to store the key and value for rock(A), paper(B), Scissor(C), and lose (X), draw (Y), win(Z)
    
    total_score = 0 # initialize the total score
    
    for i, j in rounds:
        total_score += scores[i] + scores[j]
    return total_score

# Reading the input from the file
rounds = read_input('input_3_cap1.txt')

# Calculating the total score
score = calculate_score(rounds)

# Print the total score
print(f"The total score is: {score}")

# overall Time Complexity: O(n)
        # Space Complexity: O(n)