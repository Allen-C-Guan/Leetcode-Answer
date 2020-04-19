#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <cctype>
using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        set<char> vow_dic = {'a', 'e','i', 'o', 'u'};
        int left = 0, right = s.size()-1;
        
        while (left < right){
            //调整left
            while (left < right and !vow_dic.count(tolower(s[left])))
                left ++;
            //调整right
            while (right > left and !vow_dic.count(tolower(s[right])))
                right --;
            //swap
            swap(s[left],s[right]);
            right --;
            left ++;
        }
        return s;
    }
};

//int main(){
//    Solution* s = new Solution;
//    s -> reverseVowels("leetcode");
//}
