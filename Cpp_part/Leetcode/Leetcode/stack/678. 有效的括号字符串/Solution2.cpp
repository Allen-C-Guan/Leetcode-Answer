#include <iostream>
#include <string>
#include <stack>

using namespace std;
/*
 思路为一个stack存放‘(’ 的index， 一个存放 “*” 的index。
 然后就是stack解决 （）的那一套， 不同的是如果（ stack为空，还可以试试*是否还有剩余。
 这个思路太基础了就不深讲了。

 这个题的关键在于 最后的匹配上，即当*和（都有剩余的时候如何匹配

 匹配的方式并不是唯一的，但是有最保险的匹配法
  在最后的匹配，也就是说剩下了 ( 和 *， 最保险的匹配方式在于右对齐匹配法
  即：
  '(' :   1 4 6
  '*' : 2 5 7 9
  
  其中数字为出现的index
  这种匹配方式最为保险，如果这种匹配方式都匹配不上，这就结果一定是无法匹配了。

 而这个顺序就正好是两个栈顶一一对应的顺序。

 我们最后只要关系（还剩不剩就行了。
 
*/
class Solution {
public:
    bool checkValidString(string s) {
        stack<int> s_left, s_star;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(')
                s_left.push(i);
            else if(s[i] == '*')
                s_star.push(i);
            else{                       // ")"
                if(!s_left.empty())
                    s_left.pop();
                else if (!s_star.empty())
                    s_star.pop();
                else
                    return false;
            }
        }
        while (!s_left.empty() and !s_star.empty()){
            int top_left = s_left.top(), top_star = s_star.top();
            if(s_left.top() > s_star.top()) return false;
            s_left.pop();
            s_star.pop();
        }
        
        return s_left.empty();  //最后我们只关心left是不是空就行了。
    }
};
