#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

// 冒泡
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

// 选择
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

// 堆
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

// STL堆
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

// 插入
void insert(vector<int> &arr){
    for (int i = 1; i < arr.size(); i++){
        int deal = arr[i]; // 待排序的数
        int j = i-1; // 排好序数组的末尾
        if (arr[j] > deal){
            while (j >= 0 && arr[j] > deal){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = deal;
        }
    }
}

// 归并
void merge(vector<int> &arr, int left, int mid, int right){
    vector<int> temp(right-left+1); //temp数组暂存合并的有序序列
    
    int i = left, j = mid+1, k = 0;
    while(i <= mid && j <= right){
        if (arr[i] < arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    while (i <= mid) //若比较完之后，第一个有序区仍有剩余，则直接复制到t数组中
        temp[k++] = arr[i++];
    while (j <= right)
        temp[k++] = arr[j++];
    
    for (i = left, k = 0; i <= right; i++, k++) //将排好序的存回arr中low到high这区间
        arr[i] = temp[k];
}

void mergeSort(vector<int> &arr, int left, int right){
    if (left >= right) return;
    
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid+1, right);
    merge(arr, left, mid, right);
}

// 快排
int partition(vector<int> &arr, int left, int right){
    int pivot = arr[left];
    int i = left+1, j = right;

    while (i <= j)
    {
        while (i < right && arr[i] <= pivot)
            i++;
        while (j > left && arr[j] > pivot)
            j--;
        if (i >= j) break;

        swap(arr[i], arr[j]);
    }
    swap(arr[j], arr[left]);
    return j;
}

void quickSort(vector<int> &arr, int left, int right){
    if (left >= right) return;
    
    int p = partition(arr, left, right);
    quickSort(arr, left, p-1);
    quickSort(arr, p+1, right);
}

int main(){
    vector<int> arr = {8, 1, 14, 3, 21, 5, 7, 10};
    for(auto it : arr){
        cout << it << " ";
    }
    cout << endl;;
    // bubble(arr);
    // select(arr);
    // heap(arr, arr.size());
    // insert(arr);
    // mergeSort(arr, 0, arr.size()-1);
    quickSort(arr, 0, arr.size()-1);
    for(auto it : arr){
        cout << it << " ";
    }

    // 堆排序
    // heap_stl();
    return 0;
}