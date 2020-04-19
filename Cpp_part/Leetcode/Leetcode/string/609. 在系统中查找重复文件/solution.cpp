#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <regex>
#include <algorithm>
using namespace std;


//最奇怪的就是tmd竟然超时！！！ 而且也不知道怎么超时的。

class Solution {
private:
    vector<string> split(const string& text, const string& split_flag){
        regex flag(split_flag);
        return vector<string>(sregex_token_iterator(text.begin(), text.end(), flag, -1), sregex_token_iterator());
    }
    
    void buildDic(const string root, const vector<string>& file_list, unordered_map<string, vector<string>>& dic){
        for(string each_file: file_list){
            //找括号
            int start = 0;
            while(each_file[start] != '(') start++;   //start == (
            int end = each_file.size() - 1;
            //利用括号确定key和val
            string key = each_file.substr(start+1, end),    //一定要用substr(index_begin, index_end)
                    val = root + "/" + each_file.substr(0, start);
            //update dic
            dic[key].push_back(val); //可以直接push的，用法和defaultcollection[list]一样的。
        }
    }
    
    
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> dic;
        //build dic key = root, val is files
        for(string& s: paths){
            auto splt_res = this -> split(s, "\\s+");
            this -> buildDic(splt_res[0], vector<string>(splt_res.begin()+1, splt_res.end()), dic);
        }
        
        vector<vector<string>> res;
        for(auto& same_content_list: dic){
            if(same_content_list.second.size() > 1)
                res.push_back(same_content_list.second);
        }
        return  res;
    }
};
//
//int main(){
//    Solution* s = new Solution;
//    vector<string> inputs = {"root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"};
//
//    auto res = s -> findDuplicate(inputs);
//}
//
//
