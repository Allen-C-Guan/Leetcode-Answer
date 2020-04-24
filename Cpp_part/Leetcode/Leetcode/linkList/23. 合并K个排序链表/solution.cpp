#include <iostream>
#include <queue>


using namespace std;
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x)
        : val(x), next(NULL) {}
};

/*
 这是一个非常经典的题。
 这个题的关键在于两个：
 1. 使用priority queue
 2. 穿针引线的方法
 
 处理link list的方法 接 移 断！！
 */

class Solution {
private:
    class myCmp{
    public:
        bool operator () (const ListNode* a, const ListNode* b) const{
            return a->val > b->val;
        }
    };
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode* , vector<ListNode*>, myCmp> pq;
        for(ListNode* node: lists){
            if(node != NULL) pq.push(node);
        }
        ListNode temp(-1); ListNode* pre_head = &temp; ListNode* cur = pre_head;
        //穿针引线
        while (!pq.empty()){
            ListNode* next_one = pq.top();
            cur->next = next_one;
            cur = cur->next;
            pq.pop();
            if(next_one->next != NULL) pq.push(next_one->next);
            next_one->next = NULL;
        }
        return pre_head->next;
    }
};

