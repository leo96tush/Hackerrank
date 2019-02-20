#include <bits/stdc++.h>

using namespace std;


int main(){
    int n,k,input,count=0;
    vector<int> prices;
    cin >> n >> k;
    for(int i=0;i<n;i++){
        cin >> input;
        prices.push_back(input);
    }
    sort(prices.begin(),prices.end());
    for(int i=0;i<prices.size();i++){
        if(k>prices[i]){
            count++;
            k = k - prices[i];
        }
    }
    cout << count;
    return(0);
}
