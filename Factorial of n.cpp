#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long long int n,fact=1;
    cin >> n;
    if(n==0 || n==1){
        cout << 1;
    }
    else{
        for(int i=2;i<=n;i++){
            fact = fact*i;
        }
        cout << fact;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
