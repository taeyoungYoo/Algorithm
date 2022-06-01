#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<vector<ll> > matrix;


matrix operator * (const matrix &A, const matrix &B){
    ll N = A.size();
    matrix tmp(N, vector<ll>(N));
    
    for(ll i = 0; i < N; ++i){
        for(ll j = 0; j < N; ++j){
            ll sum = 0;
            for(ll k = 0; k < N; ++k){
                sum += A[i][k] * B[k][j];
            }
            tmp[i][j] = sum % 1000;
        }
    }
    return tmp;
}

void printMatrix(const matrix& A){
    ll N = A.size();
    for(ll i = 0; i < N; ++i){
        for(ll j = 0; j < N; ++j){
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}

matrix matrixMultiplication(matrix A, int M){
    ll N = A.size();
    matrix eye(N, vector<ll>(N));
    for(ll i = 0; i < N; ++i){
        eye[i][i] = 1;
    }
    if(M == 0) return eye;
    if(M % 2 > 0) return matrixMultiplication(A, M-1) * A;
    return matrixMultiplication(A, M/2) * matrixMultiplication(A, M/2);
}

int main(){
    ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
    ll n, b;
    cin >> n >> b;

    matrix A(n, vector<ll>(n));
    for(ll i = 0; i < n; ++i){
        for(ll j = 0; j < n; ++j){
            ll input;
            cin >> input;
            A[i][j] = input;
        }
    }
    matrix R = matrixMultiplication(A, b);
    printMatrix(R);
}