#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,i,q,a,b,c;
    string name;
    cin >> n;
    map<string,int> m;
    for(i=0;i<n;i++)
    {
        cin >> q >> name;
        if(q==1)
        {
            cin >> a;
           m[name] = m[name] + a ;
        }
        else if(q==2)
        {
            m.erase(name);
        }
        else if(q==3)
        {
            cout << m[name] << "\n";
        }
        else
        {
            cout << "Wrong query number";
        }
    }
    return 0;
}



