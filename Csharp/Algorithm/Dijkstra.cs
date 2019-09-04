using System;

namespace Algorithm
{
    public class Dijkstra
    {
        public int V;

        public int minDistance(int[] dist, bool[] sptSet)
        {
            var minVal = int.MaxValue;
            var minIndex = -1;

            for (var i = 0; i < V - 1; i++)
            {
                if (sptSet[i] == false && dist[i] <= minVal)
                {
                    minVal = dist[i];
                    minIndex = i;
                }
            }

            return minIndex;
        }

        public void Initialize(int src, int[,] graph)
        {
            var dist = new int[V];
            var sptSet = new bool[V];

            for (var i = 0; i < V - 1; i++)
            {
                dist[i] = int.MaxValue;
                sptSet[i] = false;
            }

            dist[src] = 0;

            for (var count = 0; count < V - 1; count++)
            {
                var u = minDistance(dist, sptSet);

                sptSet[u] = true;

                for (var v = 0; v < V - 1; v++)
                {
                    if (sptSet[v] == false && graph[u, v] != 0 && dist[u] != int.MaxValue && dist[u] + graph[u, v] < dist[v])
                    {
                        dist[v] = dist[u] + graph[u, v];
                    }
                }
            }

            Console.WriteLine("Dijkstra");

            for (var i = 0; i < V - 1; i++)
            {
                Console.WriteLine($"{i}:{dist[i]}");
            }
        }
    }
}
