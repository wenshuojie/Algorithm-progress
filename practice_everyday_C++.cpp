#include<string>
#include<unordered_map>
#include<iostream>

using namespace std;

// 最小覆盖子串
class Solution {
  public:
    string minWindow(string S, string T) {
        unordered_map<char, int> win;
        unordered_map<char, int> need;
        for(auto t:T)
            need[t]++;

        int valid = 0;
        int left = 0, right = 0;
        int start = 0, len = INT_MAX;
        while(right < S.length()){
            char s_r = S[right++];
            if(need.count(s_r)){
                win[s_r]++;
                if(win[s_r] == need[s_r])
                    valid++;
            }

            while(valid == need.size()){
                if(right-left < len){
                    start = left;
                    len = right - left;
                }
                char s_l = S[left++];
                if(need.count(s_l)){
                    if(win[s_l] == need[s_l])
                        valid--;
                    win[s_l]--;
                }
            }
        }
        return len == INT_MAX ? "" : S.substr(start, len);
    }
};

int main()
{
    char str[] = "我的名字叫TZRG";
    cout << sizeof(str) <<endl;
    return 0;
}