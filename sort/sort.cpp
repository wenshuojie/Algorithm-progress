#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void bubble(vector<int>& arr){
    int len_vec = arr.size();
    int temp = 0;
    for (int i = 1; i < len_vec; i++){
        bool ex = false;
        for (int j = 0; j < len_vec-i; j++){
            if (arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                ex = true;;
            }
        }
        if (!ex) return;
    }
}

void select(vector<int>& arr){
    int len_vec = arr.size();
    int min_ind = 0, temp = 0, j = 0;
    for (int i = 0; i < len_vec-1; i++){
        min_ind = i;
        j = i+1;
        while (j < len_vec)
        {
            if (arr[j] < arr[min_ind]) min_ind = j;
            j ++;
        }
        if (min_ind != i){
            temp = arr[i];
            arr[i] = arr[min_ind];
            arr[min_ind] = temp;
        }
    }
}

void heap_adjust(vector<int>& arr, int len, int ind){
    int left = 2 * ind + 1, right = 2 * ind +2;
    int maxind = ind; // 三个数中的最大数的下标
    if (left < len && arr[left] > arr[maxind]) maxind = left;
    if (right < len && arr[right] > arr[maxind]) maxind = right;

    if (maxind != ind){
        swap(arr[maxind], arr[ind]);
        heap_adjust(arr, len, maxind); // 调整交换后节点的子树情况
    }
}

void heap(vector<int>& arr, int len){
    for(int i = len/2-1; i >=0; i--){
        heap_adjust(arr, len, i);
    }
    for (int i = len - 1; i >= 1; i--){
        swap(arr[0], arr[i]);
        heap_adjust(arr, i, 0);
    }
}

void heap_stl(){
    vector<int> arr = {8, 1, 14, 3, 21, 5, 7, 10};
    make_heap(arr.begin(), arr.end(), greater<int>());
    for (auto num : arr)
        cout << num << ' ';
    cout << endl;
    sort_heap(arr.begin(), arr.end(), greater<int>());
    for (auto num : arr)
        cout << num << ' ';
}

int main(){
    // vector<int> arr = {8, 1, 14, 3, 21, 5, 7, 10};
    // for(auto it : arr){
    //     cout << it << " ";
    // }
    // cout << endl;;
    // bubble(arr);
    // select(arr);
    // heap(arr, arr.size());
    // for(auto it : arr){
    //     cout << it << " ";
    // }
    heap_stl();
    return 0;
}