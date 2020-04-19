//
//  solution1.cpp
//  Leetcode
//
//  Created by Allen on 3/4/20.
//  Copyright © 2020 Allen. All rights reserved.
//
#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;
class Solution{
// 所有定义作用域都在scope里面的。
typedef vector<vector<int>> Grid;
typedef pair<int, int> Pair;
typedef vector< pair<int, int> > Stack;
    
public:
    int orangesRotting(Grid& grid) {
        // push head in queue
        int fresh_cnt = 0;
        vector< pair<int, int> > cur_level;
        for(int x = 0; x < grid.size(); x++){
            for(int y = 0; y < grid[x].size(); y ++)
                if (grid[x][y] == 2)
                    cur_level.push_back(make_pair(x, y));
                else if (grid[x][y] == 1)
                    fresh_cnt ++;
        }
        
        //BFS
        int level = -1;
        while(!cur_level.empty()){
            Stack next_level;
            for(vector< pair<int, int> >:: iterator it = cur_level.begin(); it != cur_level.end(); it++){
                this->infection(grid, next_level, (*it).first-1, (*it).second, fresh_cnt);
                this->infection(grid, next_level, (*it).first, (*it).second-1, fresh_cnt);
                this->infection(grid, next_level, (*it).first+1, (*it).second, fresh_cnt);
                this->infection(grid, next_level, (*it).first, (*it).second+1, fresh_cnt);
            }
            cur_level = next_level;
            level ++ ;
        }
        return fresh_cnt? -1 : max(level, 0);
    }
    
    // infection
    void infection(Grid& grid, Stack& next_level, const int x, const int y, int& fresh_cnt){
        // c++ 中不能使用。 b < a < c，要用&& 连接
        if ( (0 <= x && x < grid.size()) && (0 <= y && y < grid[x].size()) && (grid[x][y] == 1) ){
            next_level.push_back({x, y});
            grid[x][y] = 2;
            fresh_cnt --;
        }
    }
};








//int main() {
//    vector<vector<int>> grid = {{0}};
//    Solution* s = new Solution;
//    cout << s -> orangesRotting(grid) << endl;
//}
