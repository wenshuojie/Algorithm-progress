// 300. 最长递增子序列(LC)

#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

// int lengthOfLIS(vector<int>& nums){
    
// }

int main(){
    int test = 180, num = 2;
    while (test != 1)
    {
        while (test % num == 0)
        {
            cout << num << " ";
            test /= num;
        }
        num++;
    }
    return 0;
}