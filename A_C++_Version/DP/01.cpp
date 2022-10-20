// 从最简单的斐波那契数列入手

#include<iostream>

using namespace std;

// 递归：存在重叠子问题
int func01(int n){
    if (n == 0 || n == 1){
        return n;
    }else{
        return func01(n-1)+func01(n-2);
    }
}

// 备忘录
int helper_func02(int n, int* memo){
    if (n == 0 || n == 1) return n;
    if (memo[n] != 0) return memo[n];

    memo[n] = helper_func02(n-1, memo) + helper_func02(n-2, memo);
    return memo[n];
}

int func02(int n){
    int memo[n+1] = {0};
    return helper_func02(n, memo);
}

// DP table(自底向上)
int func03(int n){
    if (n == 0) return 0;

    int dp[n+1] = {0};
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++){
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}



int main(){

    int test01 = func01(5);
    int test02 = func02(5);
    int test03 = func03(5);

    cout << test01 << endl;
    cout << test02 << endl;
    cout << test03 << endl;
    return 0;
}