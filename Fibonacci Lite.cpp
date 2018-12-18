#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int fibonacci(int n){
    int fib[100];
    fib[0] = 0;
    fib[1] = 1;
    for(int i=2;i<=n;i++){
        fib[i] = fib[i-1]+fib[i-2];
    }
    return(fib[n]);
}

int main() {
    int n;
    cin >> n;
    cout << fibonacci(n);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
