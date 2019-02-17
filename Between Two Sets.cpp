#include <bits/stdc++.h>

using namespace std;

int gcd(int a,int b){
    if(a==b){
        return(a);
    }
    else if(a>b){
        return(gcd(a-b,b));
    }
    else{
        return(gcd(a,b-a));
    }
}

int lcm(int a,int b){
    return((a*b)/gcd(a,b));
}

int main(){
    int n,m,a[100],b[100];
    cin >> n >> m;
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    for(int i=0;i<m;i++){
        cin >> b[i];
    }
    int divisor = b[0],multiple = a[0];
    for(int i=0;i<m;i++){
        divisor = gcd(divisor,b[i]);
    }

    for(int i=0;i<n;i++){
        multiple = lcm(multiple,a[i]);
    }
    int count=0;
    for(int i=multiple;i<=divisor;i++){
        if((divisor % i) == 0) {
        count++;
        }
    }
    cout << count ;
    


}
