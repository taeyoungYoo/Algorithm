#include <iostream>
#include <vector>
#include <map>

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;

vector<int> parents(200005);
vector<int> rank_set(200005);
map<string, int> id;

int find(int u){
    if (u == parents[u]) return u;
    return parents[u] = find(parents[u]);
}

void merge(int u, int v){
    u = find(u);
    v = find(v);
    if(u == v) return;
    parents[u] = v;
    rank_set[v] += rank_set[u];
}

void getGroupNum(int u, int lim){
    int tmp = find(u), count{0};
    for(int i=1; i <= lim; ++i){
        if(find(parents[i]) == tmp) count++;
    }
    cout << count << '\n';
}

int main(){
    fastio;

    int n, m;
    cin >> n;
    for(int i = 0; i < n; ++i){
        cin >> m;
        int ptr{1};

        for(int j = 1; j <= n * m * 2; ++j){
            parents[j] = j;
            rank_set[j] = 1;
        }
        id.clear();

        for(int k = 1; k <= m; ++k){
            string a, b;
            cin >> a >> b;
            if(!id[a]){
                id[a] = ptr++;
            }
            if(!id[b]){
                id[b] = ptr++;
            }
            int u = find(id[a]), v = find(id[b]);
            if(u == v){
                cout << max(rank_set[u], rank_set[v]) << '\n';
                continue;
            }
            else{
                merge(u, v);
                cout << max(rank_set[u], rank_set[v]) << '\n';
            }
        }
    }
}