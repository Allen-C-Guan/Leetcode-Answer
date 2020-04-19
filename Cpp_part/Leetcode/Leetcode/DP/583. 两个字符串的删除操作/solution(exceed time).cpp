#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;
//暴力法！ 严重超时 DFS就是阶乘的复杂度！！就很大！

//这题思路应该是最长公共字串的问题！！！

class Solution {
private:
    void DFS(const string& word, int begin, unordered_set<string>& substr_set, string& path){
        if (begin >= word.size())
            return;
        for (int cur = begin; cur < word.size(); cur ++) {
            path += word[cur];
            substr_set.insert(path);
            this -> DFS(word, cur+1, substr_set, path);
            path.pop_back();
        }
    }
    
public:
    int minDistance(string word1, string word2) {
        unordered_set<string> substrset1, substrset2;
        string init = "";
        this -> DFS(word1, 0, substrset1, init);
        this -> DFS(word2, 0, substrset2, init);
        int max_len = 0;
        for(string cur_sub: substrset1){
            if(substrset2.count(cur_sub)){
                max_len = max(max_len, (int)cur_sub.size()); //max和min必须是同一个类型的才能比
            }
        }
        return word1.size() + word2.size() - 2 * max_len;
    }
};

//int main(){
//    Solution* s = new Solution;
//    auto res = s -> minDistance("eat", "tea");
//
//
//}
