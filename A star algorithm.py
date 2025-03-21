# -*- coding: utf-8 -*-
"""A star Algorithm

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XeRN8HPFBSbP-l69VWBq1GG8cQsbOv6j
"""

#Astar Algorithm

import heapq




def readinputfile(input_file):
    open_file=open( input_file,'r')

    overall_input=open_file.readlines()
    print(overall_input)

    huristic_value={}
    neighbour_g_nodes={} #graph nodes
    for i in overall_input :
      # print(i)
      l=i.split()
      # print(l)
      nodes=l[0]
      huristic_value[nodes]=int(l[1])
      n_value=[] #neighbours
      for j in range(2,len(l),2):
        n2_values, n_distance=l[j],int(l[j+1]) #n=neighbour
        n_value.append((n2_values,n_distance))
        # n_value[nodes]=n_value
      neighbour_g_nodes[nodes]=n_value
    return neighbour_g_nodes,huristic_value #returning


  # print(neighbour_nodes)







# print(huristic_value)
# print(neighbour_nodes)



def Astar_search(huristic_value, start_node):
    set_file = []
    heapq.heappush(set_file, (huristic_value[start_node], start_node))
    from_node = {}
    Ac = {node: float('inf') for node in huristic_value}
    Ac[start_node] = 0
    e_c = {node: float('inf') for node in huristic_value}
    e_c[start_node] = huristic_value[start_node]

    return set_file, from_node, Ac, e_c

def Astar_path(from_node, destination, Ac):
    t_path = [destination]
    c_node = destination
    while c_node in from_node:
        c_node = from_node[c_node]
        t_path.append(c_node)
    t_path.reverse()
    return t_path, Ac[destination]

# Main A* algorithm
def Astar_algorithm(neighbour_g_nodes, huristic_value, start_node, destination):
    set_file, from_node, Ac, e_c = Astar_search(huristic_value, start_node)

    while set_file:

        c_cost, c_node_name = heapq.heappop(set_file)

        if c_node_name == destination:
            return Astar_path(from_node, destination, Ac)

        # Explore neighbors of the current node
        for n, distance in neighbour_g_nodes[c_node_name]:
            new_Ac = Ac[c_node_name] + distance
            if new_Ac < Ac[n]:
                from_node[n] = c_node_name
                Ac[n] = new_Ac
                e_c[n] = Ac[n] + huristic_value[n]
                if n not in [i[1] for i in set_file]:
                    heapq.heappush(set_file, (e_c[n], n))

    return None, float('inf')

def giveninput():
    input_file = 'Input file.txt'
    output_file = 'output.txt'

    neighbour_g_nodes, heuristics = readinputfile(input_file)

    start_node = input("start: ").strip()
    destination = input("End: ").strip()

    path, t_distance = Astar_algorithm(neighbour_g_nodes, heuristics, start_node, destination)

    writeoutput(output_file, path, t_distance)



def writeoutput(output_file, path, t_distance):
    with open(output_file, 'w') as output_file:
        if path:
            # output_file.write(f"Path: {' -> '.join(path)}\n")
            # output_file.write(f"Total distance: {t_distance} km\n")
            print(f"Path: {' -> '.join(path)}")
            print(f"Total distance: {t_distance} km")
        else:
            # output_file.write("No path")
            print("No Path found")




def main():
  giveninput()


if __name__ == "__main__":
    main()