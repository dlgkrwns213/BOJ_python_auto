#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, k;
    cin >> n >> k;
    
    vector<int> lengths(n);
    for (int i = 0; i < n; ++i) {
        string name;
        cin >> name;
        lengths[i] = name.length();
    }

    vector<int> cnt(21, 0);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += cnt[lengths[i]];

        if (i >= k) {
            cnt[lengths[i - k]]--;
        }

        cnt[lengths[i]]++;
    }

    cout << total << endl;

    return 0;
}