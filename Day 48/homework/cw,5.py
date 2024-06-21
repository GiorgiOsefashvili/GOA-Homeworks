def row_weights(array):
    team1 = sum(array[i] for i in range(0, len(array), 2))
    team2 = sum(array[i] for i in range(1, len(array), 2))
    return (team1, team2)


print(row_weights([50, 60, 70, 80]))  
print(row_weights([13, 27, 49]))     
print(row_weights([70, 58, 75, 34, 91])) 
print(row_weights([29, 83, 67, 53, 19, 28, 96]))
