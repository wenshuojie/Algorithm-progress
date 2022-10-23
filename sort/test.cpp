#include <direct.h>
#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

void test_01() // 创建文件夹
{
    string folderPath = "E:\\python_workspace\\Algorithm-progress\\sort\\A"; 

    // if (0 != access(folderPath.c_str(), 0))
    // {
    //     // if this folder not exist, create a new one.
        int re = mkdir(folderPath.c_str());   // 返回 0 表示创建成功
        if (re == 0)
            cout << "创建成功 "  << re << endl;
        else
            cout << "创建失败 " << re << endl;
    // }
    
}

void test_02(){
    char str1[5] = "abcd";
    char str2[10] = "leonardo";
    strncpy(str2, str1, 3);
    cout << str1 << endl;
    cout << str2 << endl;
}

void test_03(){ // 游乐园
    /*
    先对n个数排序，然后对前n-1个数求解体积为t-1的背包问题，结果加上最后一个数即为最优解。
    测试用例 98 4417 给出答案4442，这种方法算得结果为4512，测试用例有误。
    */
    int n, t;
    cin >> n >> t;
    vector<int> p(n);
    for(int i = 0; i < n; ++i) cin >> p[i];
    sort(p.begin(), p.end());
    
    t = min(t, 10000);
    vector<int> a(t, 0);
    for(int i = 0; i < n-1; ++i){
        for(int j = t-1; j >= p[i]; --j){
            a[j] = std::max(a[j], p[i]+a[j-p[i]]);
        }
    }
    cout << (a[t-1]+p[n-1]) << endl;
}

void test_04(){
    char s[]="123456789";  
    char d[]="1234";  
    strcpy(d,s);  
    printf("d=%s,\ns=%s",d,s);  
}

int main(){
    vector<int> test(9);
    cout << test.size();
    return 0;
}