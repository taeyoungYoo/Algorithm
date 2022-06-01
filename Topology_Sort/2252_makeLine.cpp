#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int inDegree[32005], n, v;
vector<int> adjList[32005];

void topologicalSort(){
    for(int i = 1; i <= n; ++i){
        for(int &j : adjList[i])
            inDegree[j]++;
    }

    queue<int> q;
    for(int i = 1; i <= n; ++i){
        if(inDegree[i] == 0)
            q.push(i);
    }

    while(!q.empty()){
        int now = q.front(); q.pop();
        cout << now << " ";

        for(int &next : adjList[now]){
            if(--inDegree[next] == 0)
                q.push(next);
        }
    }
}

int main(){
    cin >> n >> v;
    for(int i = 0; i < v; ++i){
        int from, to;
        cin >> from >> to;
        adjList[from].push_back(to);
    }
    topologicalSort();
}