#include <iostream>
#include <vector>

using namespace std;

vector<int> relationship[101];
vector<bool> visited(101);

void DFS(int start, int end, int count){
    if(start == end){
        cout << count;
        exit(0);
    }
    visited[start] = true;
    for(int i = 0; i < relationship[start].size(); ++i){
        int next = relationship[start][i];
        if(!visited[next])
            DFS(next, end, count + 1);
    }
}

int main(){
    int n_fam, start, end, line;
    cin >> n_fam;
    cin >> start >> end;
    cin >> line;

    for(int i = 0; i < line; ++i){
        int parent, child;
        cin >> parent >> child;
        relationship[parent].push_back(child);
        relationship[child].push_back(parent);
    }
    int count{0};
    DFS(start, end, count);
    cout << -1;
}