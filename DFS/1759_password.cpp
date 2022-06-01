#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<char> vowel;
vector<char> consonant_vowel;
vector<int> visited;

int n, m;

void printVector(vector<char> print_it){
    //check if at least two consonants exist
    int limit = 0;
    for(int i=0; i < print_it.size(); ++i){
        if(visited[i] == 1 && (consonant_vowel[i] == 'a' | consonant_vowel[i] == 'e' | consonant_vowel[i] == 'i' | consonant_vowel[i] == 'o' | consonant_vowel[i] == 'u')){
            limit++;
        }
    }
    if(limit == 0 | limit > n-2){
        return;
    }
    // print vowel
    for(int i=0; i < print_it.size(); ++i){
        if(visited[i] == 1){
            cout << print_it[i];
        }
    }
    cout << endl;
}

// combination
void DFS(int node, int num){
    if(num == n){
        printVector(consonant_vowel);
        return;
    }
    for(int i=node ; i < consonant_vowel.size(); ++i){
        if(visited[i] == 1)
            continue;
        visited[i] = 1;
        DFS(i, num + 1);
        visited[i] = 0;
    }
}

int main(){
    cin >> n >> m;
    for(int i=0; i< m; i++){
        char abc;
        cin >> abc;
        consonant_vowel.push_back(abc);
        visited.push_back(0);
    }
    sort(consonant_vowel.begin(), consonant_vowel.end());
    DFS(0, 0);
}