#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool CanNadoriPang(vector<int>& basket, int N, int K, int T)
{
   sort(basket.begin(), basket.end());

   // Check the total number
   long long total = 0;
   for (auto iter = basket.begin(); iter != basket.end(); iter++)
      total += *iter;
   if (total % K != 0)
      return false;

   // Execute Nadori-Pang
   auto left = basket.begin();
   auto right = basket.end() - 1;
   int move = T;
   while (left < right)
   {
      int gap = (*left < K - *right) ? *left : K - *right;
      move -= gap;
      if (move < 0)
        return false;

      *left -= gap;
      *right += gap;

      if (*left == 0)
         left++;
      else
         right--;
         
      // cout << "hi " << *left << " " << *right << " " << move << endl;
   }
   return (*left == 0 || *left == K);
}

int main()
{
   int N, K, T;
   cin >> N >> K >> T;

   vector<int> basket(N);
   for (int i = 0; i < N; i++)
   {
      cin >> basket[i];
   }
   cout << (CanNadoriPang(basket, N, K, T) ? "YES" : "NO");
   return 0;
}