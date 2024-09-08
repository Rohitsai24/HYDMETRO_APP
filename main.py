import streamlit as st
import networkx as nx

class MetroMap:
    def __init__(self):
        self.graph = nx.Graph()
        self.create_metro_map()

    def create_metro_map(self):
        self.add_vertex("MG Bus Station")
        self.add_vertex("Shilparamam")
        self.add_vertex("Hitech City")
        self.add_vertex("Raidurg")
        self.add_vertex("LB Nagar")
        self.add_vertex("Jubilee Hills")
        self.add_vertex("Miyapur")
        self.add_vertex("KPHB")
        self.add_vertex("Paradise")
        self.add_vertex("Secunderabad")
        self.add_vertex("Koti")
        self.add_vertex("MG Road")
        self.add_vertex("Rasoolpura")
        self.add_vertex("Falaknuma")
        self.add_vertex("JBS")

        self.add_edge("MG Bus Station", "Shilparamam", 10)
        self.add_edge("Shilparamam", "Hitech City", 6)
        self.add_edge("Hitech City", "Raidurg", 4)
        self.add_edge("Raidurg", "LB Nagar", 15)
        self.add_edge("LB Nagar", "Koti", 13)
        self.add_edge("Koti", "MG Road", 5)
        self.add_edge("MG Road", "Rasoolpura", 10)
        self.add_edge("Rasoolpura", "Paradise", 6)
        self.add_edge("Paradise", "Secunderabad", 8)
        self.add_edge("Secunderabad", "Falaknuma", 12)
        self.add_edge("Falaknuma", "Jubilee Hills", 20)
        self.add_edge("Jubilee Hills", "KPHB", 16)
        self.add_edge("KPHB", "Miyapur", 10)
        self.add_edge("Hitech City", "Miyapur", 8)
        self.add_edge("Raidurg", "JBS", 9)

    def add_vertex(self, vname):
        self.graph.add_node(vname)

    def add_edge(self, vname1, vname2, value):
        self.graph.add_edge(vname1, vname2, weight=value)

    def get_minimum_distance(self, src, dst):
        length, _ = nx.single_source_dijkstra(self.graph, src, target=dst, weight='weight')
        return length

    def get_minimum_time(self, src, dst):
        length, _ = nx.single_source_dijkstra(self.graph, src, target=dst, weight='weight')
        return length / 60  # assuming 1 unit of distance = 1 minute for this example

    def get_interchanges(self, path):
        interchanges = []
        prev_line = None
        count = 0
        for i, node in enumerate(path[:-1]):
            current_line = node.split('~')[1]  # Simplified line extraction
            if prev_line and prev_line != current_line:
                interchanges.append(f"{node} ==> {path[i + 1]}")
                count += 1
            else:
                interchanges.append(node)
            prev_line = current_line
        return interchanges, count

def main():
    st.title("Hyderabad Metro Map")

    metro_map = MetroMap()

    stations = list(metro_map.graph.nodes)
    src = st.selectbox("Select Source Station", stations)
    des = st.selectbox("Select Destination Station", stations)

    if st.button("Get Shortest Distance"):
        if src and des:
            distance = metro_map.get_minimum_distance(src, des)
            st.write(f"Shortest distance from {src} to {des} is {distance} KM")

    if st.button("Get Shortest Time"):
        if src and des:
            time = metro_map.get_minimum_time(src, des)
            st.write(f"Shortest time from {src} to {des} is {time} minutes")

    if st.button("Get Shortest Path (Distance-wise)"):
        if src and des:
            path = nx.shortest_path(metro_map.graph, source=src, target=des, weight='weight')
            interchanges, count = metro_map.get_interchanges(path)
            st.write("Shortest path (distance-wise):")
            st.write(" -> ".join(interchanges))
            st.write(f"Number of interchanges: {count}")

    if st.button("Get Shortest Path (Time-wise)"):
        if src and des:
            path = nx.shortest_path(metro_map.graph, source=src, target=des, weight='weight')
            interchanges, count = metro_map.get_interchanges(path)
            st.write("Shortest path (time-wise):")
            st.write(" -> ".join(interchanges))
            st.write(f"Number of interchanges: {count}")

if __name__ == "__main__":
    main()
