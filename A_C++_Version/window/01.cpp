// NC28 最小覆盖子串

#include<iostream>
#include<string>
#include<map>

using namespace std;

string minWindow(string S, string T){
    map<char, int> need;
    map<char, int> win;
    for (auto t:T){
        need[t] ++;
    }

    int start = 0, sub_len = INT_MAX;
    int left = 0, right = 0;
    int val = 0;
    while (right < S.size()){
        char s = S[right++];
        if (need.find(s) != need.end()){
            win[s]++;
            if (win[s] == need[s]){
                val ++;
            }
        }

        // 缩小窗口
        while(val == need.size()){
            if (right-left < sub_len){
                start = left;
                sub_len = right - left;
            }

            char s = S[left++];
            if(need.find(s) != need.end()){
                if(win[s] == need[s]){
                    val --;
                }
                win[s]--;
            }
        }


    }

    return sub_len == INT_MAX ? "" : S.substr(start, sub_len);
}

int main(){
    cout << "RESULT:" << minWindow("XDOYEZODEYXNZ","XYZ") << endl;
    return 0;
}