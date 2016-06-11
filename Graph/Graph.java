import java.io.*;
import java.util.*;

/*
 * Implementation of Graph data structure.
 *
 */
public class Graph() {
    
    private int vertex;
    private LinkedList<Integer> adj[];

    /*
     * Constructor.
     *
     */
    Graph(int vertex) {
        this.vertex = vertex;
        this.adj = new LinkedList<Integer>[vertex];
        for(int i=0; i<vertex; i++) {
            this.adj[i] = new LinkedList<Integer>();
        }
    }

    /*
     * Return the number of vertices.
     *
     */
    public int countVertex() {
        return this.vertex;
    }

    /*
     * Return the number of edges.
     *
     */
    public int countEdges() {
        continue;
    }

    /*
     * Add a new edge between two vertices.
     *
     */
    public void addEdge(int src, int dest) {
        this.adj[src].add(dest)
    }

    /*
     * Remove an edge from the graph.
     *
     */
    public removeEdge() {
        continue;
    }

    /*
     * Perform breadth first search.
     *
     */
    public void bfs() {

    }

	public static void main(String[] args) {
        Graph gr = new Graph();
        gr.addEdge(0, 1);
        gr.addEdge(0, 2);
        gr.addEdge(2, 0);
        gr.addEdge(2, 3);
        gr.addEdge(3, 3);
        gr.addEdge(1, 2);
        
        gr.bfs();
	}
}
