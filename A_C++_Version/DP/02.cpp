// 322. 零钱兑换(LC)

#include<iostream>
#include<vector>

using namespace std;

int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount+1, amount+1);

    dp[0] = 0;
    for (int i = 0; i < dp.size(); i++){
        for (int coin : coins){
            if (i-coin < 0) continue;
            dp[i] = min(dp[i-coin]+1, dp[i]);
        }
    }

    return dp[amount] == amount+1 ? -1 : dp[amount];
}

int main(){
    vector<int> coins = {1, 2, 5};
    int amount = 11;
    cout << coinChange(coins, amount);
    return 0;
}