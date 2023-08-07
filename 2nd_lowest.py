if __name__ == '__main__':
    marksheet = []  # Initialize an empty list to store name-score pairs
    scoresheet = []  # Initialize an empty list to store scores
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])  # Append the name-score pair to the marksheet list
        scoresheet.append(score)  # Append the score to the scoresheet list
        
    # Get the unique scores and sort them
    unique_scores = sorted(set(scoresheet))
    
    # Find the second lowest score
    second_lowest_score = unique_scores[1]
    
    # Filter students with the second lowest score and sort by name
    students_with_second_lowest = sorted([name for name, score in marksheet if score == second_lowest_score])
    
    # Print the names of students with the second lowest score
    for student in students_with_second_lowest:
        print(student)
