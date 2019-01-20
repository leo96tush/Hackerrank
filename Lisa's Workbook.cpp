#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k, i;
  cin >> n >> k;
  int ar[n];
  for (i = 0; i < n; i++)
    cin >> ar[i];

  int p = 1, c = 0, j = 0, m = 1;
  for (i = 0; i < n; i++) {
    m = 1;
    while (m <= ar[i]) {
      for (j = 1; j <= k && m <= ar[i]; j++) {
        if (m == p) {
          c += 1;
        }
        m += 1;
      }
      p += 1;
    }
  }
  cout << c;
  return 0;
}
