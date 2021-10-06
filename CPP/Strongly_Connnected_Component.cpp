// Strongly Connectd Components

#include<bits/stdc++.h>
using namespace std;

// Kosaraju's Algorithm -----------------------------------------------------
// for forming stack
int dfs(vector<int > graph[ ], int visited[ ], stack<int > &st, int &src)
{
	visited[src]=1;
	for(int j=0;j<graph[src].size();j++)
	{
		if(!visited[graph[src][j]])
		dfs(graph, visited, st, graph[src][j]);
	}
	st.push(src);
}

// for printing the answer of all strongly connected components
int dfs1(vector<int > graph1[ ], int visited1[ ], int &src)
{
	visited1[src]=1;
	cout<<src<<" ";
	for(int j=0;j<graph1[src].size();j++)
	{
		if(!visited1[graph1[src][j]])
		dfs1(graph1, visited1, graph1[src][j]);
	}
}

int main()
{
	// kosaraju's Algorithm
	int n = 11;
	vector<int > graph[n];
	graph[0].push_back(1);
	graph[1].push_back(2);
	graph[2].push_back(0);
	graph[1].push_back(3);
	graph[3].push_back(4);
	graph[4].push_back(5);
	graph[5].push_back(3);
	graph[6].push_back(5);
	graph[6].push_back(7);
	graph[7].push_back(8);
	graph[8].push_back(9);
	graph[9].push_back(6);
	graph[9].push_back(10);
	// here while doing same DFS as topological sort, but it is not always a topological sort, because here graph can be any graph not always DAG
	
	// DFS
	int visited[n] = {0};
	stack<int > st;
	for(int i=0;i<n;i++)
	{
		if(!visited[i])
		dfs(graph, visited, st, i);
	}
	
	// reversing the graph
	vector<int > graph1[n];
	graph1[1].push_back(0);
	graph1[2].push_back(1);
	graph1[0].push_back(2);
	graph1[3].push_back(1);
	graph1[4].push_back(3);
	graph1[5].push_back(4);
	graph1[3].push_back(5);
	graph1[5].push_back(6);
	graph1[7].push_back(6);
	graph1[8].push_back(7);
	graph1[9].push_back(8);
	graph1[6].push_back(9);
	graph1[10].push_back(9);
	
	// popping one by one element from stack and doing dfs with the reverse graph.
	int visited1[n] = {0};
//	cout<<"stack\n";
	while(!st.empty())
	{
		int x = st.top();
//		cout<<x<<endl;
		st.pop();
		if(!visited1[x])
		{
			dfs1(graph1, visited1, x);
			cout<<endl;
		}
		
	}
	
	
	return 0;
}
