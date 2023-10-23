# import test
#
# adj = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
#
# test.print_distance(adj)

# import math
#
#
# class TSPSolver:
#     def __init__(self, adj_matrix):
#         self.adj_matrix = adj_matrix
#         self.num_cities = len(adj_matrix)
#         self.visited = [False] * self.num_cities
#         self.final_path = [None] * (self.num_cities + 1)
#         self.final_res = float('inf')
#
#     def first_min(self, i):
#         min_val = float('inf')
#         for k in range(self.num_cities):
#             if self.adj_matrix[i][k] < min_val and i != k:
#                 min_val = self.adj_matrix[i][k]
#         return min_val
#
#     def second_min(self, i):
#         first, second = float('inf'), float('inf')
#         for j in range(self.num_cities):
#             if i == j:
#                 continue
#             if self.adj_matrix[i][j] <= first:
#                 second = first
#                 first = self.adj_matrix[i][j]
#             elif self.adj_matrix[i][j] <= second and self.adj_matrix[i][j] != first:
#                 second = self.adj_matrix[i][j]
#         return second
#
#     def tsp_recursion(self, curr_bound, curr_weight, level, curr_path):
#         if level == self.num_cities:
#             if self.adj_matrix[curr_path[level - 1]][curr_path[0]] != 0:
#                 curr_res = curr_weight + self.adj_matrix[curr_path[level - 1]][curr_path[0]]
#                 if curr_res < self.final_res:
#                     self.final_path = curr_path[:]
#                     self.final_path[level] = curr_path[0]
#                     self.final_res = curr_res
#             return
#
#         for i in range(self.num_cities):
#             if self.adj_matrix[curr_path[level - 1]][i] != 0 and not self.visited[i]:
#                 temp = curr_bound
#                 curr_weight += self.adj_matrix[curr_path[level - 1]][i]
#
#                 if level == 1:
#                     curr_bound -= (self.first_min(curr_path[level - 1]) + self.first_min(i)) / 2
#                 else:
#                     curr_bound -= (self.second_min(curr_path[level - 1]) + self.first_min(i)) / 2
#
#                 if curr_bound + curr_weight < self.final_res:
#                     curr_path[level] = i
#                     self.visited[i] = True
#
#                     self.tsp_recursion(curr_bound, curr_weight, level + 1, curr_path)
#
#                 curr_weight -= self.adj_matrix[curr_path[level - 1]][i]
#                 curr_bound = temp
#
#                 self.visited = [False] * self.num_cities
#                 for j in range(level):
#                     if curr_path[j] != -1:
#                         self.visited[curr_path[j]] = True
#
#     def solve_tsp(self):
#         curr_bound = 0
#         curr_path = [-1] * (self.num_cities + 1)
#
#         for i in range(self.num_cities):
#             curr_bound += self.first_min(i) + self.second_min(i)
#
#         curr_bound = math.ceil(curr_bound / 2)
#
#         self.visited[0] = True
#         curr_path[0] = 0
#
#         self.tsp_recursion(curr_bound, 0, 1, curr_path)
#
#     def get_minimum_cost(self):
#         return self.final_res
#
#     def get_optimal_path(self):
#         return self.final_path
#
#
# # Example usage
# adj_matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
#
# solver = TSPSolver(adj_matrix)
# solver.solve_tsp()
#
# minimum_cost = solver.get_minimum_cost()
# optimal_path = solver.get_optimal_path()
#
# print("Minimum cost:", minimum_cost)
# print("Optimal path:", optimal_path)

a = 27570.0



s = str(a)
print(s[0:2])
