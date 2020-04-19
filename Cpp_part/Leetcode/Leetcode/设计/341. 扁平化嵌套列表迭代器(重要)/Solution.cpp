#include <iostream>
#include <vector>
#include <stack>

using namespace std;


// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
class NestedInteger {
public:
  // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;

  // Return the single integer that this NestedInteger holds, if it holds a single integer
  // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;

  // Return the nested list that this NestedInteger holds, if it holds a nested list
  // The result is undefined if this NestedInteger holds a single integer
    const vector<NestedInteger> &getList() const;  //第一个const说返回的必须是个const，第个const说不能改变当前类里的内容。
};




/*
 这道题有两个关键点：
 1. 每次调用next之前，都会调用has next function
 2. 这是个迭代器， 迭代器是什么？ 不能一次把所有的内容都处理了啊。应该是走一步处理一步才是迭代器的正确工作方式
 
 因此这个题的正确思路是：
 1. 利用has_next function来实现next step的处理， 把一切准备工作都做好
 2. 括号的展开方法为： 每次只展开一层括号，反向遍历并压入stack，而后工作方式和BFS相似。 pop一个，然后展开，并把展开项压入stack。
 
 */



class NestedIterator {
private:
    stack<NestedInteger> stk;   //reverse_it 竟然和it是两个class！！！ 他们之间是继承关系！！
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for(vector<NestedInteger>::reverse_iterator it = nestedList.rbegin(); it != nestedList.rend(); it++){
            stk.push(*it);
        }
    }

    int next(){
        int next_val = stk.top().getInteger();
        stk.pop();
        return next_val;
    }
    
    bool hasNext() {
        if(stk.empty()) return false;

        while(!stk.top().isInteger()){  //迭代展开到stack顶第一个是int就停止了
            vector<NestedInteger> next_level = stk.top().getList();
            stk.pop();

            for(auto it = next_level.rbegin(); it != next_level.rend(); it ++)
                stk.push(*it);
            
            if (stk.empty()) return false;  //这就是为了防止[[]]的情况，这种情况就是拆到最后，stack里啥也不剩了
        }
        return true;
    }
};



