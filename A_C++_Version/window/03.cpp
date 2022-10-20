// 3. 无重复字符的最长子串 (leetcode)
#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int lengthOfLongestSubstring(string s) {
    map<int, int> win;
    int left = 0, right = 0;
    int sub_len = 0;

    while(right < s.size()){
        char c = s[right++];
        win[c]++;
        while (win[c] > 1){
            win[s[left++]]--;
        }
        sub_len = max(sub_len, right-left);
    }
    return sub_len;
}

int main(){
    cout << lengthOfLongestSubstring("abcabcbb") << endl;
    return 0;
}