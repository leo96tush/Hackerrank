#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> a;
    vector<int>::iterator it;
    int n,k;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> k;
        a.push_back(k);    
    }
    sort(a.begin(),a.end());
    /*for(it=a.begin();it!=a.end();++it){
        cout << *it << " ";
    }*/
    int max = -100,length=0;
    for(int i=0;i<a.size();i++){
        for(int j=i;j<a.size();j++){
            if((a[j]-a[i])==0 || (a[j]-a[i])==1){
                length++;
            }
        }
        if(max<=length){
            max = length;
        }
        length = 0;
    }
    cout << max;
    
}
