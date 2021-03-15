
### load packages ###
# system tools
import os

# data analysis
import pandas as pd

# for plotting networks
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz

# for parsing arguments
import argparse

# for combining dictionaries
from collections import defaultdict


### Define main function ###

def main():
    
    
    # Initialise argumentparser
    ap = argparse.ArgumentParser()
    # Define arguments
    ap.add_argument("-i", "--infile", required=False, help="Input filename", type = str, default="data/weighted_edgelist.csv")
    ap.add_argument("-op", "--outfile_plot", required=True, help="Output plot filename", type = str)
    ap.add_argument("-oc", "--outfile_csv", required=True, help="Output csv filename")
    ap.add_argument("-w", "--weight_cutoff", required=False, help="Weight cutoff", default=500, type=int)

    # Parse arguments to args
    args = vars(ap.parse_args())
    
    # define the weight cutoff (minimum weight)
    weight_cutoff = args["weight_cutoff"]
    
    # start message
    print("\nBEGINNING...")
    
    # Input filename
    input_file = args["infile"]
    
    # start message
    print("\nReading in data...")
    
    # make file into df
    data = pd.read_csv(input_file)
        
    # filter out just the ones with weights higher than the chosen weight cutoff
    filtered_df = data[data["weights"] > weight_cutoff]

    #### plotting the filtered df as a graph #### 
    # create a graph object 
    graph_object = nx.from_pandas_edgelist(filtered_df, "nodeA", "nodeB", ["weights"])  
     
    print("\nMaking plot...")          
    # plot the graph object 
    pos = nx.nx_agraph.graphviz_layout(graph_object, prog="neato")
    nx.draw(graph_object, pos, with_labels=True, node_size=20, font_size=10)
    
    
    # Output plot filename
    out_file_name_plot = args["outfile_plot"]
    # Create directory called viz, if it doesn't exist
    if not os.path.exists("viz"):
        os.mkdir("viz")
    
    # Output plot filepath
    outfile1 = os.path.join("viz", out_file_name_plot)
    
    print("\nSaving plot...")
    # save plot  
    plt.savefig(outfile1, dpi=300, bbox_inches='tight')
    
    
    
    print("\nInitialising analysis of centrality, betweenness and eigenvector values...")
    #### get centrality betweenness and eigenvector values ###
    
    # calculate metrics
    degree = nx.degree_centrality(graph_object)
    betweenness = nx.betweenness_centrality(graph_object)
    eigenvector = nx.eigenvector_centrality(graph_object)
    # make into dataframe
    df = pd.DataFrame({
        "degree":pd.Series(degree),
        "betweenness":pd.Series(betweenness),
        "eigenvector":pd.Series(eigenvector)  
        })
    
    # Output csv filename
    out_file_name_csv = args["outfile_csv"]
    # Create directory called output, if it doesn't exist
    if not os.path.exists("output"):
        os.mkdir("output")    
        
    # Output csv filepath
    outfile2 = os.path.join("output", out_file_name_csv)
    
    # save df as .csv-file 
    df.to_csv(outfile2, sep='\t', encoding='utf-8')

    
# Define behaviour when called from command line
if __name__=="__main__":
    main()
    
    
    
    
    
    