# Multiple-Source Personalized PageRank

## Introduction

This project implements a multiple-source personalized PageRank algorithm using a Hadoop multi-node cluster. Personalized PageRank is an extension of the traditional PageRank algorithm that incorporates a personalized bias towards a specific set of source nodes. This approach is useful for applications where the relevance of nodes is dependent on their proximity to a particular set of important nodes.

## Objective

The objective of this project is to compute the personalized PageRank values for a set of nodes in a network, biased towards a specific set of source nodes. This involves setting up a three-node Hadoop cluster (one master and two slaves) and executing a MapReduce program to calculate the personalized PageRank.

## Methodology

1. **Setup Hadoop Cluster**:
    - Install and configure Hadoop on all nodes.
    - Enable password-less SSH between the master and slave nodes.
    - Configure the Hadoop settings (`core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, `yarn-site.xml`).
    - Start Hadoop services using `start-dfs.sh` and `start-yarn.sh`.

2. **Prepare Input Data**:
    - Use the dataset provided in themassignment, formatted for Hadoop processing.

3. **Implement MapReduce Program**:
    - **Mapper (`mapper.py`)**:
        - Read the input file and create a dictionary with nodes and their adjacency lists.
        - Output each node and its adjacency list for the reducer.
    - **Reducer (`reducer.py`)**:
        - Read the mapper output and initialize PageRank values, giving higher weight to source nodes.
        - Compute personalized PageRank using an iterative approach biased towards source nodes.
        - Output the final personalized PageRank values for each node.

4. **Run the MapReduce Job**:
    - Compile the mapper and reducer scripts.
    - Submit the job to the Hadoop cluster using the Hadoop streaming jar.

## Technologies Used

- **Hadoop**: A framework for distributed storage and processing of large datasets using the MapReduce programming model.
- **Python**: Programming language used for implementing the mapper and reducer scripts.
- **SSH**: Secure Shell, used for configuring password-less access between Hadoop nodes.

## Conclusion

Personalized PageRank provides a method to compute the importance of nodes in a network with a bias towards a specific set of nodes, making it more suitable for applications requiring personalized or user-specific results. The project successfully demonstrates the implementation of this algorithm using a Hadoop multi-node cluster, highlighting the practical applications of distributed computing in handling large-scale graph processing tasks.
