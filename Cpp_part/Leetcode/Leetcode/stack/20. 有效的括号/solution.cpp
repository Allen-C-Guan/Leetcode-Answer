#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<char> path;
        unordered_map<char, char> dic = {{'(',')'}, {'{', '}'}, {'[', ']'}};
        for(char c: s){
            if (dic.count(c))
                path.push(c);
            else if (!path.empty() and c == dic[path.top()])
                path.pop();
            else
                return false;
        }
        return path.empty();
    }
};

//int main(){
//    Solution* s = new Solution;
//    auto res = s -> isValid("()");
//    cout << res << endl;
//}
