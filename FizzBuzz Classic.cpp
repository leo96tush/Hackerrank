#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        if(i%3==0 && i%5!=0){
            cout << "Fizz" << endl;
        }
        else if(i%3!=0 && i%5==0){
            cout << "Buzz" << endl;
        }
        else if(i%3==0 && i%5==0){
            cout << "FizzBuzz" << endl;
        }
        else{
            cout << i << endl;
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
