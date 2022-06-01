#include <iostream>
#include <vector>

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;

vector<int> parent(201);
vector<int> route(1001);

int find(int u){
    if(u == parent[u]) return u;
    return parent[u] = find(parent[u]);
}

void merge(int u, int v){
    u = find(u);
    v = find(v);
    if(u == v) return;
    parent[u] = v;
}

int main(){
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; ++i){
        parent[i] = i;
    }
    for(int i = 1; i <= n; ++i){
        for(int j = 1; j <= n; ++j){
            int input;
            cin >> input;
            if(i==j) continue;
            else if(input == 1){
                merge(i, j);
            }
        }
    }
    for(int i = 0; i < m; ++i){
        cin >> route[i];
    }
    bool isPossible = true;
    for(int i = 0; i <m-1; ++i){
        if(find(route[i]) != find(route[i+1])) isPossible = false;
    }
    if(isPossible){
        cout << "YES";
        return 0;
    }
    cout << "NO";
}