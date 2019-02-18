#include <bits/stdc++.h>

using namespace std;

// Complete the beautifulBinaryString function below.
int beautifulBinaryString(string b) {
    int count = 0,n;
    n = b.length();
    for (int i = 2; i < n; i++) {
        if (b[i] == '0' && b[i - 2] == '0' && b[i - 1] == '1') {
            count++;
            i += 2;
    }
  }
  return(count);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string b;
    getline(cin, b);

    int result = beautifulBinaryString(b);

    fout << result << "\n";

    fout.close();

    return 0;
}
