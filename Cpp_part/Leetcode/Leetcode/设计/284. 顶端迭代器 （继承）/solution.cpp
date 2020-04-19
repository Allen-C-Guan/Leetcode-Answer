#include <iostream>
#include <vector>
using namespace std;

//这个方法的精髓在于用子类和父类的copy constructor来新建一个和当前完全的类。


//这就是一个class的声明！！！  除了body，竟然都写全了。。。。c++ 竟然有这么蠢的声明方式。。。

class Iterator {
public:
    struct Data;
    Data* data;
    Iterator(const vector<int>& nums);
    Iterator(const Iterator& iter);  //这个constructor的功能一定是copy一个完全相同的it，包括当前迭代的位置和当前的其中的全部内容。
    // Returns the next element in the iteration.
    int next();
    // Returns true if the iteration has more elements.
    bool hasNext() const;
};


class PeekingIterator : public Iterator {
public:
    PeekingIterator(const vector<int>& nums) : Iterator(nums) {
        
    }
    // Returns the next element in the iteration without advancing the iterator.
    int peek() {
        if(this -> hasNext()){
            Iterator new_it(*this);
                // *this表示是子类自己， 而父类有copy constructor, 这里就直接调用了copy constructor新建了一个。两个不同的it自然互不影响
                // Iterater( Iterator&  child) 因为是继承，这个函数就可以这么用。
            return new_it.next();
        }
        return NULL;
    }
    
    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    int next() {
        return Iterator::next();
        //这是调用父类的方法，和java 的super功能相同，但是这个方式可以用在任何class上。双冒号前的class的名字，后面是该class中的function。
    }
    
    bool hasNext() const {
        return Iterator::hasNext();
    }
};


