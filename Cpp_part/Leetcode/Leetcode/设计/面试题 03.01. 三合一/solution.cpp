#include <utility>
using namespace std;

class TripleInOne {
private:
    int base;
    pair<int, int> bot_top[3];  //first bot, second top
    int* trip_stack;
public:
    TripleInOne(int stackSize){
        base = stackSize;
        trip_stack = new int[base*3];
        bot_top[0] = make_pair(0, -1);
        bot_top[1] = make_pair(base, base-1);
        bot_top[2] = make_pair(base*2, base*2-1);
    }
    
    void push(int stackNum, int value) { // 满的时候啥也不做
        if(bot_top[stackNum].second < (stackNum+1) * base - 1)
            trip_stack[++bot_top[stackNum].second] = value;
    }
    
    int pop(int stackNum) { //空的时候要返回-1
        if(this->isEmpty(stackNum))
            return -1;
        else
            return trip_stack[bot_top[stackNum].second --];
    }
    
    int peek(int stackNum) { //空的时候要返回-1
        if(this->isEmpty(stackNum))
            return -1;
        else
            return trip_stack[bot_top[stackNum].second];
    }
    
    bool isEmpty(int stackNum) {
        return bot_top[stackNum].first > bot_top[stackNum].second;
    }
};
