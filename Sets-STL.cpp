#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n,i,q,a,b,c;
    cin >> n;
    set<int> s;
    for(i=0;i<n;i++)
    {
        cin >> q;
        if(q==1)
        {
           cin >> a;
           s.insert(a);            
        }
        else if(q==2)
        {
            cin >> b ;
            s.erase(b);
        }
        else if(q==3)
        {
            cin >> c;
            cout << (s.find(c) == s.end() ? "No" : "Yes") << endl;
        }
        else
        {
            cout << "Wrong query number";
        }
    }
    return 0;
}



