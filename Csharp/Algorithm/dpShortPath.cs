using System;
using System.Collections.Generic;
using System.Linq;

namespace Algorithm
{
    public class DPShortPath
    {
        public class Edge
        {
            public string src, dest;

            public int layer;

            public float weight;
        }

        public class Graph
        {
            public List<Edge> edges = new List<Edge>();

            public int layerCout;
        }

        public static float Fn(Graph graph, string src, int layer)
        {
            if (layer == graph.layerCout)
            {
                return 0;
            }

            var edges = graph.edges.FindAll(val => val.layer == layer & & val.src == src);

            return edges.Min(val => (val.weight + Fn(graph, val.dest, layer + 1)));
        }

        public static void Init()
        {
            var graph = new Graph
            {
                layerCout = 3
            };

            //A->B
            graph.edges.Add(new Edge()
            {
                src = "A",
                dest = "B",
                layer = 0,
                weight = 4
            });

            //A->C
            graph.edges.Add(new Edge()
            {
                src = "A",
                dest = "C",
                layer = 0,
                weight = 2
            });

            //B->E
            graph.edges.Add(new Edge()
            {
                src = "B",
                dest = "E",
                layer = 1,
                weight = 3
            });

            //B->D
            graph.edges.Add(new Edge()
            {
                src = "B",
                dest = "D",
                layer = 1,
                weight = 7
            });

            //C->D
            graph.edges.Add(new Edge()
            {
                src = "C",
                dest = "D",
                layer = 1,
                weight = 5
            });

            //E->F
            graph.edges.Add(new Edge()
            {
                src = "E",
                dest = "F",
                layer = 2,
                weight = 4
            });

            //D->F
            graph.edges.Add(new Edge()
            {
                src = "D",
                dest = "F",
                layer = 2,
                weight = 3
            });

            Console.WriteLine(Fn(graph, "A", 0));
        }
    }
}
