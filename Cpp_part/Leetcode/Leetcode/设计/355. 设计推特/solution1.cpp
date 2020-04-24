#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

/*
 //这里，
 1. 各自的推文用list好过用vector。  因为没有查找和索引的需求，而list的多路并归在这里也非常的重要。
 2. follower没有顺序要求，自然用set
 3. id与内容之间，自然就用map来提供。

 因此这里 这里最重要的点在于多路并归，以及set和map的选用。


 */

class Twitter {
public:
    /** Initialize your data structure here. */
    // key: userId  value.first = 自己的推特list （推特id， 顺序）,   value.second = follower.list
    unordered_map<int, pair<vector<pair<int, int>>, unordered_set<int>>> database;
    int cnt = 0;
    Twitter() {
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        database[userId].first.push_back(make_pair(tweetId, cnt++));
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<pair<int, int>> tweet_list;
        tweet_list = database[userId].first;
        
        for(int followerId: database[userId].second){
            for(auto tweet: database[followerId].first){
                tweet_list.push_back(tweet);
            }
        }
        sort(tweet_list.begin(), tweet_list.end(), [](pair<int, int> a, pair<int, int> b){
            return a.second > b.second;
        });
        
        vector<int> news_list;
        int i = 0;
        while (i < 10 and i < tweet_list.size()){
            news_list.push_back(tweet_list[i++].first);
        }
        return news_list;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if(followerId == followeeId) return;
        database[followerId].second.insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        database[followerId].second.erase(followeeId);
    }
};


//int main(){
//    Twitter* obj = new Twitter();
//    obj->postTweet(1,5);
//    vector<int> param_2 = obj->getNewsFeed(1);
//    obj->postTweet(2, 6);
//    obj->follow(1,2);
//    vector<int> param_3 = obj->getNewsFeed(1);
//    obj->unfollow(1,2);
//    vector<int> param_4 = obj->getNewsFeed(1);
//}
