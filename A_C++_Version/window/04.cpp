// 567. 字符串的排列 (leetcode)
#include<iostream>
#include<string>
#include<map>

using namespace std;

bool checkInclusion(string s1, string s2) {
    map<char, int> need;
    map<char, int> win;
    for (auto c : s1){
        need[c]++;
    }

    int left = 0, right = 0;
    int valid = 0;
    while (right < s2.size()){
        char c = s2[right++];
        if (need.count(c)){
            win[c]++;
            if (win[c] == need[c])
                valid++;
        }

        // 收缩窗口
        if (right-left == s1.size())
        {
            if (valid == need.size()) return true;

            char c = s2[left++];
            if (need.count(c)){
                if (win[c] == need[c])
                    valid--;
                win[c]--;
            }
        }
    }
    return false;
}

int main(){
    cout << boolalpha << checkInclusion("ab", "eidbaooo") << endl;
    cout << boolalpha << checkInclusion("ab", "eidboaooo") << endl;
    return 0;
}