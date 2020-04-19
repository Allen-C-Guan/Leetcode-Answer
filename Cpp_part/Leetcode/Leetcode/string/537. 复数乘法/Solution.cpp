#include<iostream>
#include<string>
#include <utility>
#include <cctype>
using namespace std;

//stoi 可以把string

class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        auto a_num = this -> decodeCplx(a), b_num = this -> decodeCplx(b);
        int first_res = a_num.first * b_num.first - a_num.second * b_num.second;
        int second_res = a_num.first * b_num.second + a_num.second * b_num.first;
        return to_string(first_res) + '+' + to_string(second_res) + 'i';
    }
    
private:
    pair<int, int> decodeCplx(string& s){
        //decode first one
        // decode first one sign
        int cur = 0;
        pair<string, string> pre_res = {"", ""};
       
        bool is_first_neg = false, is_sec_neg = false;
        
        if(!isalnum(s[cur])){
            if(s[cur] == '-'){
                is_first_neg = true;
                cur ++;
            }
        }
        //decode first num
        while (isdigit(s[cur]) ){
            pre_res.first += s[cur];
            cur ++;
        }
        // decode second
        if(!isalnum(s[cur+1])){
            if (s[cur+1] == '-')
                is_sec_neg = true;
            cur += 2;
        }else
            cur ++;
        
        while(isdigit(s[cur])){
            pre_res.second += s[cur];
            cur ++;
        }
        
        pair<int, int> res = {stoi(pre_res.first), stoi(pre_res.second)};
        if(is_first_neg)
            res.first *= -1;
        if (is_sec_neg)
            res.second *= -1;
        return res;
    }

};



//int main(){
//    Solution* s = new Solution;
//    auto res = s -> complexNumberMultiply("1+1i", "2+3i");
//
//}
