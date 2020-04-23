#include <forward_list>
#include <utility>
using namespace std;

class MyHashMap {
public:

    forward_list<pair<int, int>> my_map[2068];

    MyHashMap() {
    }
    
    int hashFunction(int key){
        return key % 2069;
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int index = this -> hashFunction(key);
        //空
        if(my_map[index].empty()){
            my_map[index].push_front(make_pair(key, value));
            return;
        }
        
        //有相同的时候
        for(auto& cur_pair: my_map[index]){
            if(cur_pair.first == key){
                cur_pair.second = value;
                return;
            }
        }
        //无相同
        my_map[index].push_front(make_pair(key, value));
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        for(auto cur_pair: my_map[hashFunction(key)]){
            if(cur_pair.first == key) {
                return cur_pair.second;
            }
        }
        return -1;
    }
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        my_map[hashFunction(key)].remove_if([&](pair<int, int> p){return p.first == key;});
    }
};
//
//
//int main(){
//    MyHashMap* m = new MyHashMap;
//    
//    m -> put(2, 2);
//    m -> put (2, 1);
//}
