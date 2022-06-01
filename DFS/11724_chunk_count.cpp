#include <iostream>
#include <vector>

using namespace std;

vector<int> vec_check[1001];
bool visited[1000];

void Dfs(int node){
    visited[node] = true;
    for(int i = 0; i < vec_check[node].size(); i++){
        int next = vec_check[node][i];
        if(!visited[next]){
            Dfs(next);
        }
    }
}

int main(){
    int n, m;
    cin >> n >> m;

    int x, y;
    for(int i = 0; i < m; ++i){
        cin >> x >> y;
        vec_check[x].push_back(y);
        vec_check[y].push_back(x);
    }

    // count the possible execution of DFS
    int count{0};
    for(int i = 1; i <= n; ++i){
        if(!visited[i]){
            Dfs(i);
            count++;
        }
    }
    cout << count;
    return 0;
}
