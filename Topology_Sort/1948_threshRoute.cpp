#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;

typedef long long ll;
typedef vector<vector<int> > matrix;

const int LIMIT = 10001;
vector<int> adjList[LIMIT];
vector<int> revList[LIMIT];
matrix timeList(LIMIT, vector<int>(LIMIT));
vector<int> inDegree(LIMIT);
vector<int> minPath(LIMIT);
vector<bool> visited(LIMIT);

void topology(int cities, int start){
    for(int i = 1; i <= cities; ++i){
        for(int &j : adjList[i])
            inDegree[j]++;
    }
    queue<int> q;
    q.push(start);
    while(!q.empty()){
        int now = q.front(); q.pop();
        for(int &next : adjList[now]){
            minPath[next] = max(minPath[next], minPath[now] + timeList[now][next]);
            if(--inDegree[next] == 0) q.push(next);
        }
    }
}

int full_path;
void bfs(int cities, int start){
    queue<int> q;
    q.push(start);

    while(!q.empty()){
        int now = q.front(); q.pop();
        for(int &next : revList[now]){
            if(minPath[now] == minPath[next] + timeList[next][now]) {
                full_path++;
                if(!visited[next]){
                    q.push(next);
                    visited[next] = true;
                }
            }
        }
    }
}

int main(){
    fastio;

    int cities{0}, road{0};
    cin >> cities >> road;
    for(int i = 1; i <= road; ++i){
        int from, to, time;
        cin >> from >> to >> time;
        adjList[from].push_back(to);
        revList[to].push_back(from);
        timeList[from][to] = time;
    }
    int start, end;
    cin >> start >> end;
    topology(cities, start);
    cout << minPath[end] << endl;
    bfs(cities, end);
    cout << full_path;
}