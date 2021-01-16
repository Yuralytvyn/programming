class Node_Distance :

    def __init__(self, name, dist) :
        self.name = name
        self.dist = dist

class Graph :

    def __init__(self, node_count) :
        self.adjlist = {}
        self.node_count = node_count

    def Add_Into_Adjlist(self, src, node_dist) :
        if src not in self.adjlist :
            self.adjlist[src] = []
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path(self, source) :


        distance = [999999999999] * self.node_count
        distance[source] = 0


        dict_node_length = {source: 0}

        while dict_node_length:


            source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
            del dict_node_length[source_node]

            for node_dist in self.adjlist[source_node] :
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist


                if distance[adjnode] > distance[source_node] + length_to_adjnode :
                    distance[adjnode] = distance[source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        for i in range(self.node_count) :
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))

def main() :


    amount,connections = list(map(int, input("\nEnter the amount of vertexes and connections : ").strip().split()))


    choose_who_are_clients = list(map(int, input("\nEnter the numbers who are clients : ").strip().split()))

    g = Graph(amount)

    for i in range(connections):
        graph = list(map(int, input("\nEnter the graph who are clients : ").strip().split()))*3
        for i in range(len(graph)):
            start=graph[0]
            end=graph[1]
            distance=graph[2]
            g.Add_Into_Adjlist(start,Node_Distance(end,distance))

    for i in range(len(choose_who_are_clients)):
        g.Dijkstras_Shortest_Path(choose_who_are_clients[i])





if __name__ == "__main__" :
   main()

