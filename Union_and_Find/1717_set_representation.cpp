#include <iostream>
#include <vector>

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;

vector<int> parent(1'000'001);

int find(int u){
    if(u == parent[u]) return u;
    return parent[u] = find(parent[u]);
}

void merge(int u, int v){
    u = find(u);
    v = find(v);
    if(u==v) return;
    parent[u] = v;
}

int main(){
    fastio;

    int n, m;
    cin >> n >> m;
    for(int i = 1; i <=n; ++i){
        parent[i] = i;
    }
    for(int i = 0; i < m; ++i){
        int relation, node_u, node_v;
        cin >> relation >> node_u >> node_v;
        if(relation == 0){
            merge(node_u, node_v);
        }
        else{
            if(find(node_u) == find(node_v)) cout << "YES\n";
            else cout << "NO\n";
        }
    }
}