#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

vector<ll> merge_vec(500010);
vector<ll> tmp_vec(500010);
ll swap_count;

void merge(int start, int end){
    int mid = (start + end) / 2;
    int left_idx = start;
    int right_idx = mid + 1;
    int sort_idx = start;

    while(left_idx <= mid && right_idx <= end){
        if(merge_vec[left_idx] <= merge_vec[right_idx]){
            tmp_vec[sort_idx++] = merge_vec[left_idx++];
        }
        else{
            tmp_vec[sort_idx++] = merge_vec[right_idx++];
            swap_count += (mid - left_idx + 1);
        }
    }
    if(left_idx <= mid){
        for(int i = left_idx; i <= mid; ++i)
            tmp_vec[sort_idx++] = merge_vec[i];
    }
    else{
        for(int i = right_idx; i <= end; ++i)
            tmp_vec[sort_idx++] = merge_vec[i];
    }

    for(int i = start; i<=end; ++i)
        merge_vec[i] = tmp_vec[i];
}

void partition(int start, int end){
    if(start < end){
        int mid = (start + end)/2;
        partition(start, mid);
        partition(mid+1, end);
        merge(start, end);
    }
}

int main(){
    ios::sync_with_stdio(0);
	cin.tie(0);

    int n;
    cin >> n;
    for(int i = 1; i<=n;++i){
        cin >> merge_vec[i];
    }
    partition(1, n);
    cout << swap_count;
}