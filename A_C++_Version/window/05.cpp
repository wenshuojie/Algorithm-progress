// 438. 找到字符串中所有字母异位词

#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;

vector<int> findAnagrams(string s, string p) {
    map<char, int> need;
    map<char, int> win;
    for (auto c : p){
        need[c]++;
    }

    int left = 0, right = 0;
    int valid = 0;
    vector<int> res;

    while (right < s.size()){
        char c = s[right++];
        if (need.count(c)){
            win[c]++;
            if (win[c] == need[c])
                valid++;
        }

        if (right-left == p.size()){
            if (valid == need.size())
                res.push_back(left);

            char c = s[left++];
            if (need.count(c)){
                if (win[c] == need[c])
                    valid--;
                win[c]--;
            }
        }
    }

    return res;
}

int main(){
    vector<int> res = findAnagrams("cbaebabacd", "abc");
    cout << '[' ;
    for(vector<int>::iterator it = res.begin(); it != res.end(); it++){
        if (it != res.end()-1)
            cout << *it << ',';
        else
            cout << *it ;
    }
    cout << ']' ;

    return 0;
}