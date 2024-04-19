#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <vector>
using namespace std;

int DP(const vector<int>& v, const int N, const int K)
{
   vector<int> dp(K+1, -1);
   dp[0] = 0;
   for (int i = 0; i < N; i++)
   {
      for (int j = v[i]; j <= K; j++)
      {
         if (dp[j - v[i]] < 0)
            continue;
         
         if (0 < dp[j] && dp[j] <= dp[j-v[i]])
            continue;

         dp[j] = dp[j-v[i]] + 1;
      }
   }
   return dp[K];
}

int main()
{
   int N, K;
   cin >> N >> K;

   // Input data and Remove duplicates
   unordered_set<int> s;
   for (int i = 0; i < N; i++)
   {
      int x;
      cin >> x;
      s.insert(x);
   }
   vector<int> v(s.begin(), s.end());
   sort(v.begin(), v.end());
   
   // Solve using dp
   N = v.size();
   cout << DP(v, N, K) << '\n';
   return 0;
}