//This method is only possible , here assumed that all the vertices are reachable from source vertex
//Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph
#include<bits/stdc++.h>
using namespace std;
void addedge(vector<int > adj[ ],int u,int w)
{
	adj[u].push_back(w);
	adj[w].push_back(u);
}
void bfs(vector<int > adj[ ],int v,int src)
{
	bool visited[v];
	memset(visited,false,sizeof(visited));
	
	queue<int> q;
	q.push(src);
	visited[src] = true;
	while(!q.empty())
	{
		src = q.front();
		q.pop();
		cout<<src<<" ";
		for(int i=0;i<adj[src].size();i++)
		{
			if(!visited[adj[src][i]])
			{
				visited[adj[src][i]] = true;
				q.push(adj[src][i]);
			}
		}
	}
}
int main()
{
	int v = 6;
	vector<int > adj[v];
	addedge(adj,0,5);
	addedge(adj,0,1);
	addedge(adj,1,2);
	addedge(adj,1,4);
	addedge(adj,2,4);
	addedge(adj,2,3);
	addedge(adj,3,4);
	
	
	for(int i=0;i<v;i++)
	{
		cout<<"BFS with source as "<<i<<" -> "; 
		bfs(adj,v,i);
		cout<<endl;
	}
	return 0;
}
