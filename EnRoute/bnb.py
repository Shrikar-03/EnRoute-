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

import math

class TravelingSalesmanProblem:

    def __init__(self, adj):
        self.adj = adj
        self.N = len(adj)
        self.maxsize = float('inf')
        self.final_path = [None] * (self.N + 1)
        self.visited = [False] * self.N
        self.final_res = self.maxsize

    def copyToFinal(self, curr_path):
        self.final_path[:self.N + 1] = curr_path[:]
        self.final_path[self.N] = curr_path[0]

    def firstMin(self, i):
        min_val = self.maxsize
        for k in range(self.N):
            if self.adj[i][k] < min_val and i != k:
                min_val = self.adj[i][k]
        return min_val

    def secondMin(self, i):
        first, second = self.maxsize, self.maxsize
        for j in range(self.N):
            if i == j:
                continue
            if self.adj[i][j] <= first:
                second = first
                first = self.adj[i][j]
            elif self.adj[i][j] <= second and self.adj[i][j] != first:
                second = self.adj[i][j]
        return second

    def TSPRec(self, curr_bound, curr_weight, level, curr_path):
        if level == self.N:
            if self.adj[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + self.adj[curr_path[level - 1]][curr_path[0]]
                if curr_res < self.final_res:
                    self.copyToFinal(curr_path)
                    self.final_res = curr_res
            return

        for i in range(self.N):
            if self.adj[curr_path[level - 1]][i] != 0 and not self.visited[i]:
                temp = curr_bound
                curr_weight += self.adj[curr_path[level - 1]][i]

                if level == 1:
                    curr_bound -= ((self.firstMin(curr_path[level - 1]) + self.firstMin(i)) / 2)
                else:
                    curr_bound -= ((self.secondMin(curr_path[level - 1]) + self.firstMin(i)) / 2)

                if curr_bound + curr_weight < self.final_res:
                    curr_path[level] = i
                    self.visited[i] = True
                    self.TSPRec(curr_bound, curr_weight, level + 1, curr_path)

                curr_weight -= self.adj[curr_path[level - 1]][i]
                curr_bound = temp

                self.visited = [False] * len(self.visited)
                for j in range(level):
                    if curr_path[j] != -1:
                        self.visited[curr_path[j]] = True

    def solve(self):
        curr_bound = 0
        curr_path = [-1] * (self.N + 1)

        for i in range(self.N):
            curr_bound += (self.firstMin(i) + self.secondMin(i))

        curr_bound = math.ceil(curr_bound / 2)

        self.visited[0] = True
        curr_path[0] = 0

        self.TSPRec(curr_bound, 0, 1, curr_path)

    def get_minimum_cost(self):
        return self.final_res

    def get_path_taken(self):
        return self.final_path

# Driver code




