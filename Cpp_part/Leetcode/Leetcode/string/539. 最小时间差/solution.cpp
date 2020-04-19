#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <iterator>

using namespace std;

//并不知道为啥不行。。。

class Solution {
private:
    struct myCmp{
        bool operator () (pair<int, int> a, pair<int, int> b){
            if (a.first < b.first){
                return true;
            }else{
                if(a.first > b.first)
                    return false;
                else  //equal
                    return a.second < b.second;
            }
        }
    };
    
    pair<int, int> toIntPair(const string& time){
        string fst = "", sec = "";
        int cur = 0;
        while (time[cur] != ':'){
            fst += time[cur];
            cur ++;
        }
        cur ++;
        while(cur < time.size()){
            sec += time[cur];
            cur ++;
        }
        return pair<int, int>(stoi(fst), stoi(sec));
    }

    int findDiff(const pair<int, int>& a, const pair<int, int>& b ){
        return abs((a.first * 60 + a.second) - (b.first * 60 + b.second));
        
    }
    
public:
    int findMinDifference(vector<string>& timePoints) {
        set<pair<int, int>, myCmp> time_list;
        for(string cur_time: timePoints){
            time_list.insert(this -> toIntPair(cur_time));
        }
        
        //获取end的it的方法
        auto it_end = time_list.end();
        advance(it_end, -1);
        
        //处理第一个和最后一个
        int res = this -> findDiff(*time_list.begin(), *it_end);
        res = min(res, abs(res - 24*60));
        
        //处理其余的
        auto left = time_list.begin(), right = time_list.begin();
        advance(right, 1);
        
        for(;right != time_list.end(); right++){
            res = min(res, this -> findDiff(*right, *left));
            left ++;
        }
        
        return res;
    }
};


//int main(){
//    Solution* s = new Solution;
//    vector<string> inputs = {"23:59","00:00"};
//    auto res = s -> findMinDifference(inputs);
//    cout << res << endl;
//
//
//
//}
