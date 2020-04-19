#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

/*unordered_set
 这些容器使用的套路都差不多，就是
 1. 一般情况下的初始化： collection <type> name = {   };
 2. 都可以使用iterator的方法来初始化 :   collection <type> (iterator.begin(), iterator.end())
 3. iterator 的使用方法都是  collection <type> :: iterator it = .....
 
 */
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() != unordered_set<int>(nums.begin(),nums.end()).size();
    }
};
