#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int count_chunk;

vector<int> linked_list[105];
vector<bool> visited(105);

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while(!q.empty()){
        int now = q.front();
        q.pop();
        //cout << "NOW : " << now << endl;

        for(int &next : linked_list[now]){
            if(!visited[next]){
                visited[next] = true;
                q.push(next);
                count_chunk++;
            }
        }
    }
}

int main(){
    int e, v;
    cin >> e >> v;
    for(int i=0; i < v; ++i){
        int from, to;
        cin >> from >> to;
        linked_list[from].push_back(to);
        linked_list[to].push_back(from);
    }
    BFS(1);
    cout << count_chunk;
}