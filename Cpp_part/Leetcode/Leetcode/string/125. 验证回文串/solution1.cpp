#include<cctype>
#include<iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string temp;
        for(char c: s){
            if(isalnum(c))
                temp += toupper(c);  //这地方，由于你加在了string上，他会自动cast成为char。
        }
        for (int i = 0; i < (int)(temp.size()/2); i++){
            if(temp[i]!= temp[temp.size()-1-i])
                return false;
        }
        return true;
    }
};
//
//int main(){
//    Solution* s = new Solution;
//    s -> isPalindrome("A man, a plan, a canal: Panama");
//    
//}
//
