#include <vector>
#include <string>
#include<algorithm>

using namespace std;

class Solution {
private:
    int timeToInt(const string& time){
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
        return stoi(fst)*60 + stoi(sec);
    }
    
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> time_list;
        for (auto cur_time: timePoints){
            time_list.push_back(this -> timeToInt(cur_time));
        }
        
        sort(time_list.begin(), time_list.end(), less<int>());
        int min_gap = time_list[0] + 24 * 60 - time_list[time_list.size()-1];
        for(int i = 1; i < time_list.size(); i ++){
            min_gap = min(time_list[i] - time_list[i-1], min_gap);
        }
        return min_gap;
    }
};
