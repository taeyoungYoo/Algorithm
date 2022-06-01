#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int dr[4] = {0,0,1,-1};
int dc[4] = {1,-1,0,0};
vector<int> box[1001];
vector<bool> visited[1001];
int width, height, date;

struct pos{
    int r, c;
};

queue<pos> q_bfs;

void checkFresh(int w, int h){
    int tmp = 0;
    for(int i=0; i<h; ++i){
        for(int j=0;j<w;++j){
            if(box[i][j] == 0){
                cout << -1;
                exit(0);
            }
        }
    }
}

int checkMax(int w, int h){
    int tmp = 0;
    for(int i=0; i<h; ++i){
        for(int j=0;j<w;++j){
            if(tmp < box[i][j])
                tmp = box[i][j];
        }
    }
    return tmp-1;
}

void bfs(){
    while(!q_bfs.empty()){
        // just add
        pos now = q_bfs.front(); q_bfs.pop();
        for(int i = 0; i < 4; ++i){
            int nr = now.r + dr[i];
            int nc = now.c + dc[i];

            if(nr < 0 || nr >= height || nc < 0 || nc >= width)
                continue;
            else if(visited[nr][nc] || box[nr][nc] == -1)
                continue;
            box[nr][nc] = box[now.r][now.c] + 1;
            visited[nr][nc] = true;
            q_bfs.push({nr, nc});
        }
    }
}

int main(void){
    cin >> width >> height;
    bool isFresh = false;
    for(int i =0; i < height; ++i){
        for(int j = 0; j < width; ++j){
            int m;
            cin >> m;
            box[i].push_back(m);
            if(m == 1){
                q_bfs.push({i, j});
                visited[i].push_back(true);
            }
            else if(m==-1){
                visited[i].push_back(true);
            }
            else{
                visited[i].push_back(false);
                isFresh = true;
            }
        }
    }
    if(!isFresh){
        cout << 0;
        return 0;
    }
    bfs();
    checkFresh(width, height);
    date = checkMax(width, height);
    cout << date;
}