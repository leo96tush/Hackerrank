#include <bits/stdc++.h>

using namespace std;

// Complete the camelcase function below.
int camelcase(string s) {
    int length_of_string,count=0;
    length_of_string = s.length();
    for(int i=0;i<length_of_string;i++){
        if(isupper(s[i])!=0){
            count++;
        }
    }
    return(count+1);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = camelcase(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
