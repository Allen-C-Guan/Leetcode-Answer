#include <iostream>
#include <string>
#include <stack>

using namespace std;

/*
 我这是采用的双向检查法
 
 这是因为这个逻辑的逻辑漏洞与顺序有关。。。
 
 这个方法，我们只考虑用 * 去当作 ）的逻辑，没有考虑到用*当 （ 的逻辑。
 */
class Solution {
public:
    bool checkValidString(string s) {
        stack<char> stk_forward;
        int cnt = 0;
        for(char c: s){
            if(c == '(')
                stk_forward.push('(');
            else if(c == ')'){
                if(!stk_forward.empty()) stk_forward.pop(); //非空
                // * 当作 ( 的情况
                else if (cnt > 0) cnt --;   // 空 但是cnt还有
                else return false;       //空还没cnt了。
                
            }else // *
                cnt ++;
        }
        
        stack<char> stk_bkwrd;
        int cnt2 = 0;
        for(int i = s.size()-1; i > -1; i-- ){
            if(s[i] == ')' )
                stk_bkwrd.push(')');
                else if (s[i] == '('){
                    if (!stk_bkwrd.empty()) stk_bkwrd.pop();
                    else if(cnt2 > 0 ) cnt2 --;
                    else return false;
                }else
                    cnt2 ++;
        }
        return stk_forward.size() >= 0 and stk_bkwrd.size() >= 0;
    }
};
//
//int main(){
//    Solution* s = new Solution;
//    auto res = s -> checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*");
//
//
    
//}
