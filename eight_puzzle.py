import numpy as np
import copy

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank space
]

# Calculate Manhattan distance as the heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Ignore the blank tile
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Find the possible moves
def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing algorithm
def hill_climbing(start_state):
    current_state = start_state
    current_cost = manhattan_distance(current_state)
    steps = [current_state]
    
    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_cost = float('inf')
        
        for neighbor in neighbors:
            cost = manhattan_distance(neighbor)
            if cost < next_cost:
                next_cost = cost
                next_state = neighbor
        
        # Check if the best neighbor is better than the current state
        if next_cost < current_cost:
            current_state = next_state
            current_cost = next_cost
            steps.append(current_state)
        else:
            # Reached a plateau or local maximum
            break
    
    return steps, current_cost

# Display the state
def display_state(state):
    for row in state:
        print(row)
    print()

# Main function to test the algorithm
if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    
    print("Initial State:")
    display_state(initial_state)
    
    steps, final_cost = hill_climbing(initial_state)
    
    print("Steps to solution:")
    for step in steps:
        display_state(step)
    
    if final_cost == 0:
        print("Solution found!")
    else:
        print("Algorithm terminated at a local maximum or plateau.")
