#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct elecInfo{
    int u, v, w;
};

vector<elecInfo> elecLine;
vector<int> parents(1001);

bool compare(elecInfo a, elecInfo b) { return a.w < b.w;}

int find(int u){
    if(u == parents[u]) return u;
    return parents[u] = find(parents[u]);
}

void merge(int u, int v){
    u = find(u);
    v = find(v);
    parents[u] = v;
}

int main(){
    int n, m, n_power;
    cin >> n >> m >> n_power;
    for(int i =1; i <= n; ++i){
        parents[i] = i;
    }
    int tmp;
    cin >> tmp;
    for(int i = 1; i < n_power; ++i){
        int a;
        cin >> a;
        parents[a] = tmp;
    }
    for(int i = 0; i < m; ++i){
        int u, v, w;
        cin >> u >> v >> w;
        elecLine.push_back({u, v, w});
    }
    sort(elecLine.begin(), elecLine.end(), compare);
    int ret = 0;
    for(elecInfo &a : elecLine){
        if(find(a.u) != find(a.v)){
            ret += a.w;
            merge(a.u, a.v);
        }
    }
    cout << ret;
}