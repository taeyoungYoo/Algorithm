#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> realtionship[12];
vector<int> population(12);
vector<int> nodes;
vector<bool> visited(12);
int node, count_chunk, min_diff{800};


void checkDiff(const vector<int> &section_1, const vector<int> &section_2){
    int sum_1{0}, sum_2{0};
    for(int i : section_1){
        sum_1 += population[i];
    }
    for(int i : section_2){
        sum_2 += population[i];
    }
    int diff = ((sum_1 > sum_2) ? sum_1 - sum_2 : sum_2 - sum_1);
    min_diff = ((min_diff > diff) ? diff: min_diff);
}

bool BFS(const vector<int> &section){
    vector<bool> visited_section(12, 0);
    queue<int> q;
    q.push(section[0]);
    visited_section[section[0]] = true;
    int count = 1;
    while(!q.empty()){
        int now = q.front();
        q.pop();
        for(int &next : realtionship[now]){
            if(!visited_section[next] && find(section.begin(), section.end(), next) != section.end()){
                visited_section[next] = true;
                q.push(next);
                count++;
            }
        }
    }
    if(section.size() != count)
        return false;
    return true;
}

void checkLinked(){
    vector<int> section_1, section_2;
    for(int i = 1; i < nodes.size(); ++i){
        if(visited[i] == 1)
            section_1.push_back(i);
        else
            section_2.push_back(i);        
    }
    if(BFS(section_1) && BFS(section_2)){
        checkDiff(section_1, section_2);
    }
}

void combination(int node, int cnt, int lim){
    if(cnt == lim){
        // check relationship with bfs
        checkLinked();
        return;
    }
    for(int i = node; i < nodes.size(); ++i){
        if(visited[i] == 1)
            continue;
        visited[i] = 1;
        combination(i, cnt + 1, lim);
        visited[i] = 0;
    }
}

int main(){
    cin >> node;
    for(int i = 1; i <= node; ++i){
        cin >> population[i];
    }
    nodes.push_back(0);
    for(int i = 1; i <= node; ++i){
        int line;
        cin >> line;
        nodes.push_back(i);
        for(int j = 0; j < line; ++j){
            int m;
            cin >> m;
            realtionship[i].push_back(m);
        }
    }
    for(int i = 1; i < node / 2 + 1; ++i)
        combination(1, 0, i);
    if(min_diff == 800){
        cout << -1;
        return 0;
    }
    cout << min_diff;
}