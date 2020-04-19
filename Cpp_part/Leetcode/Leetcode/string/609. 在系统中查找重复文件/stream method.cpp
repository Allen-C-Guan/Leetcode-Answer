#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>

/*
 这道题中最重要的是内容就是stream的使用， stream的使用可以归结如下几个关键点
 1. stream的输出是通过 >> 来输出的
 2. stream的工作方式和it相似，都是可以记录运行到哪了。
 3. stringstream每步的停止点是 空格， 回车和分隔符，且不关心有几个空格，连续的一律抹掉
 */

using namespace std;

class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& path) {
        int n = path.size();
        unordered_map<string,vector<string>> dic;
        vector<vector<string>> res;
        for(int i = 0; i<n; i ++){
            stringstream ss(path[i]);
            string root, cur_file;
            ss >> root;            //stream的赋值是通过 << 这是对stream的overloading 来实现的
            while(ss >> cur_file){ //这是sstream的常用使用方式，类似于iterator的赶脚，当后面没有后续了以后，这个循环就结束了。
                int start = 0;
                while(cur_file[start] != '(') start ++;
                dic[cur_file.substr(start+1, cur_file.size()-1)].push_back(root + "/" + cur_file.substr(0, start));
            }
        }
        //output
        for(auto &x:dic) if(x.second.size()>1) res.push_back(x.second); //根据题意有两个及以上相同内容的才满足
        return res;
    }
};


//
//int main(){
//    Solution* s = new Solution;
//    vector<string> inputs = {"root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"};
//    auto res = s -> findDuplicate(inputs);
//}
//
//
