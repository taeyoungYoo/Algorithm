#include <iostream>
#include <vector>
#include <set>

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;

vector<int> parents(500'001);
// set<int> input_nodes;
int cycle_time = 0;

int find(int u){
    if(u == parents[u]) return u;
    return parents[u] = find(parents[u]);
}

void merge(int u, int v){
    u = find(u);
    v = find(v);
    if(u == v) return;
    parents[u] = v;
}

int main(){
    fastio;

    int n, m;
    cin >> n >> m;

    for(int i=0; i < n; ++i){
        parents[i] = i;
    }

    for(int i=0; i < m; ++i){
        int a, b;
        cin >> a >> b;
        if(find(a) == find(b)){
            cycle_time = i + 1;
            break;
        }
        merge(a, b);
    }
    cout << cycle_time;
}