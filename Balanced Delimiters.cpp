#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include<bits/stdc++.h> 
using namespace std;

bool balanced(string input_string){
    stack<char> s;
    char x;
    for(int i=0;i<input_string.length();i++){
        if(input_string[i]=='(' ||input_string[i]=='{'||input_string[i]=='['){
            s.push(input_string[i]);
        }
        
        switch(input_string[i])
        {
            case ')':
                x = s.top();
                s.pop();
                if(x=='{'||x=='[')
                {
                    return(false);
                }
                break;
            case '}':
                x = s.top();
                s.pop();
                if(x=='('||x=='[')
                {
                    return(false);
                }
                break;
            case ']':
                x = s.top();
                s.pop();
                if(x=='('||x=='{')
                {
                    return(false);
                }
                break;
                
        }
    }
    return(s.empty());
}
int main() {
    char input_string[100];
    cin >> input_string;
    if(balanced(input_string)){
        cout << "True" ;    
    }
    else{
        cout << "False";
    }
    
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
