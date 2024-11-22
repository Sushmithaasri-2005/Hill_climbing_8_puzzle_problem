# Hill_climbing_8_puzzle_problem
The Hill Climbing algorithm uses a heuristic to decide the next move, focusing on states closer to the goal state. However, it has limitations like local maxima, plateaus, and ridges.
 Heuristic Function:
•	Manhattan Distance: Measures the sum of distances of each tile from its goal position.
Algorithm Steps:
•	Start from an initial state.
•	Generate all valid neighbor states.
•	Evaluate the heuristic for each neighbor and move to the neighbor with the lowest heuristic value.
•	Stop when no better neighbor exists (plateau or local maximum).
 Limitations:
•	Local Maxima: The algorithm might get stuck in a suboptimal configuration.
•	Plateaus: When multiple states have the same heuristic value, the algorithm may fail to proceed.
•	Ridges: Steep paths that are hard to climb due to limited heuristic improvement.
