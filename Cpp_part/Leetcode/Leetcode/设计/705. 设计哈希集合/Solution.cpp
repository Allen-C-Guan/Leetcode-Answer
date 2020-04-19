#include <iostream>
#include <forward_list>

using namespace std;

class MyHashSet {
public:
    
    forward_list<int> set[1000];
    /** Initialize your data structure here. */
    MyHashSet() {
    }
    
    int hashFunction(const int& key){
        return key%1000;            // index
    }
    
    void add(int key) {
        if(this -> contains(key)) return;
        set[hashFunction(key)].push_front(key);
    }
    
    void remove(int key) {
        int idx = hashFunction(key);
        if(set[idx].empty()) return;
        set[idx].remove(key);
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int idx = hashFunction(key);
        for(int k: set[idx]){
            if (k == key)
                return true;
        }
        return false;
    }
};


