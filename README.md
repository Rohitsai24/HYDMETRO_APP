# Hyderabad Metro Map Application

## Overview

This application provides a visualization of the Hyderabad metro map and allows users to calculate the shortest distance and time between stations. Built using Streamlit and NetworkX, the app lets users:

- Select source and destination stations.
- Get the shortest distance and time between selected stations.
- View the shortest path (both distance-wise and time-wise) including the number of interchanges.

## Features

- **Shortest Distance Calculation**: Computes the shortest distance between two stations.
- **Shortest Time Calculation**: Estimates the shortest time required to travel between two stations.
- **Shortest Path (Distance-wise)**: Displays the shortest path between stations based on distance, along with interchanges.
- **Shortest Path (Time-wise)**: Shows the shortest path based on estimated travel time, including interchanges.

## Installation

To run the application, you need to have Python installed. You can then install the required libraries using pip:

```bash
pip install streamlit networkx
