#include <iostream>

using namespace std;

struct Edge
{
    string src, dest;
    
    float weight;
};

struct Graph
{
    // V-> Number of vertices, E-> Number of edges
    int V, E;

    // graph is represented as an array of edges.
    struct Edge *edge;
};

struct Graph *createGraph(int V, int E)
{
    struct Graph *graph = new Graph;
    graph->V = V;
    graph->E = E;
    graph->edge = new Edge[E];
    return graph;
}

int main()
{
    int V = 6;
    int E = 7;

    struct Graph *graph = createGraph(V, E);

    graph->edge[0].src = "A";
    graph->edge[0].dest = "B";
    graph->edge[0].weight = 4;

    graph->edge[1].src = "A";
    graph->edge[1].dest = "C";
    graph->edge[1].weight = 2;

    graph->edge[2].src = "B";
    graph->edge[2].dest = "E";
    graph->edge[2].weight = 2;

    graph->edge[3].src = "B";
    graph->edge[3].dest = "D";
    graph->edge[3].weight = 7;

    graph->edge[4].src = "C";
    graph->edge[4].dest = "D";
    graph->edge[4].weight = 5;

    graph->edge[5].src = "E";
    graph->edge[5].dest = "F";
    graph->edge[5].weight = 4;

    graph->edge[6].src = "D";
    graph->edge[6].dest = "F";
    graph->edge[6].weight = 3;

}