#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> adjList[501];
vector<int> time_consumption(501);
vector<int> min_time(501);
vector<int> inDegree(501);

void topology(int N){
    for(int i = 1; i <= N; ++i){
        for(int &j : adjList[i]){
            inDegree[j]++;
        }
    }
    queue<int> q;
    for(int i = 1; i <= N; ++i){
        if(inDegree[i] == 0) q.push(i);
    }

    while(!q.empty()){
        int now = q.front(); q.pop();
        for(int &next : adjList[now]){
            min_time[next] = max(min_time[next], min_time[now] + time_consumption[next]);
            if(--inDegree[next] == 0) q.push(next);
        }
    }
    for(int i = 1; i <= N; ++i){
        cout << min_time[i] << endl;
    }
}

int main(){
    int N;
    cin >> N;
    for(int i = 1; i <= N; ++i){
        cin >> time_consumption[i];
        min_time[i] = time_consumption[i];
        int m;
        cin >> m;
        while(m != -1){
            adjList[m].push_back(i);
            cin >> m;
        }
    }
    topology(N);
}