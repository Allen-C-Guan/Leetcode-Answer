#include <iostream>
#include <string>

#include <unordered_map>

using namespace std;

void countChar(const char& c, unordered_map<char, int>& m_map){
    if(m_map.count(c)){
        m_map[c] += 1;
    }else{
        m_map[c] = 1;
    }
}

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> count_ran, count_mag;
        for (auto c: ransomNote){
            countChar(c, count_ran);
        }
        
        for (auto c: magazine){
            countChar(c, count_mag);
        }
        
        for (auto p: count_ran){
            if (! count_mag.count(p.first) or count_mag[p.first] < p.second )
                return false;
        }
        return true;
    }
};



//int main (){
//    Solution* s = new Solution;
//    s -> canConstruct("a", "b");
//    
//    
//}
