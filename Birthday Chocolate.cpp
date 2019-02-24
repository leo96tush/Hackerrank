#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

int main(){
    int n,s[100],d,m,sum,count=0;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> s[i];
    }
    cin >> d >> m;
    for(int i=0;i<=(n-m);i++){
        sum = 0;
        for(int j=0;j<m;j++){
            sum = sum+s[i+j];
        }
        if(sum==d){
            count++;
        }
    }
    cout << count;
}
