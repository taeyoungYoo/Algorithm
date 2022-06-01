#include <iostream>
#include <vector>
#include <map>

using namespace std;

map<string, vector<string> > relationship;    // 가족 정보
map<string, double> blood;
string royal;
double bloodPercent = 0.0;

double getBlood(string name){
    double names_blood = 0.0;
    if(relationship[name].empty()){
        return blood[name];
    }
    string mom = relationship[name][0];
    string dad = relationship[name][1];
    names_blood = (getBlood(mom) + getBlood(dad))/2;
    blood[name] = names_blood;
    return names_blood;
}

int main(){
    int n, m;
    string king;
    cin >> n >> m;
    cin >> king;
    for(int i = 0; i < n; ++i){
        string child, mom, dad;
        cin >> child >> mom >> dad;
        relationship[child].push_back(mom);
        relationship[child].push_back(dad);
        blood[child] = blood[mom] = blood[dad] = 0;
    }
    blood[king] = 1;
    for(int i = 0; i < m; ++i){
        string name;
        cin >> name;
        double tmp = getBlood(name);
        if(tmp > bloodPercent){
            royal = name;
            bloodPercent = tmp;
        }
        else continue;
    }
    cout << royal;
}