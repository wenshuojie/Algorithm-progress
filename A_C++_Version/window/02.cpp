// NC41 最长无重复子数组

#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int maxLength(vector<int>& arr) {

    map<int, int> win;
    int left = 0, right = 0;
    int sub_len = 0;
    int arrLen = arr.size();

    while (right < arrLen)
    {
        int num = arr[right++];
        win[num]++;

        while(win[num] > 1){
            win[arr[left++]]--;
        }
        sub_len = sub_len > (right-left) ? sub_len : (right-left);
    }
    
    return sub_len;
}

int main(){
    vector<int> arr = {1,2,3,1,2,3,2,2};
    cout << maxLength(arr) << endl;
    return 0;
}