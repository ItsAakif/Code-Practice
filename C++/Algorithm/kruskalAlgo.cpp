#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
struct Edge {
    int src, dest, weight;
};

// Structure to represent a disjoint set
struct DisjointSet {
    vector<int> parent, rank;
    
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

// Kruskal's algorithm to find the minimum spanning tree
void kruskalMST(vector<Edge>& edges, int numVertices) {
    sort(edges.begin(), edges.end(), [](Edge a, Edge b) {
        return a.weight < b.weight;
    });
    
    vector<Edge> mst; // Minimum Spanning Tree
    DisjointSet ds(numVertices);
    
    for (Edge edge : edges) {
        int srcRoot = ds.find(edge.src);
        int destRoot = ds.find(edge.dest);
        
        if (srcRoot != destRoot) {
            mst.push_back(edge);
            ds.unionSets(srcRoot, destRoot);
        }
    }
    
    cout << "Edges in the Minimum Spanning Tree:" << endl;
    for (Edge edge : mst) {
        cout << edge.src << " - " << edge.dest << " : " << edge.weight << endl;
    }
}

int main() {
    // Example usage
    int numVertices = 6;
    vector<Edge> edges = {
        {0, 1, 4},
        {0, 2, 4},
        {1, 2, 2},
        {1, 0, 4},
        {2, 0, 4},
        {2, 1, 2},
        {2, 3, 3},
        {2, 5, 2},
        {2, 4, 4},
        {3, 2, 3},
        {3, 4, 3},
        {4, 2, 4},
        {4, 3, 3},
        {5, 2, 2}
    };
    
    kruskalMST(edges, numVertices);
    
    return 0;
}
