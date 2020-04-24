#include <iostream>
#include <stack>
using namespace std;

//左右手互导
class MyQueue {
public:
    stack<int> queue;
    stack<int> helper;
    
    /** Initialize your data structure here. */
    MyQueue() {
    }
    /** Push element x to the back of queue. */
    void push(int x) {
        if(queue.empty())
            queue.push(x);
        else{  //queue 非空
            while(!queue.empty()){
                helper.push(queue.top());
                queue.pop();
            }
            helper.push(x);
            
            while(!helper.empty()){
                queue.push(helper.top());
                helper.pop();
            }
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int top = queue.top();
        queue.pop();
        return top;
    }
    
    /** Get the front element. */
    int peek() {
        return queue.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return queue.empty();
    }
};
