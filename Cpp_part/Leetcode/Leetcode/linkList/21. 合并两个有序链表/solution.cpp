#include <iostream>
#include <memory>
using namespace std;


struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};
/*
注意这个方法过后l1和l2就断了，因为cur采用侵占下一node,然后再下一个node上 原地修改next的方法。因此并没有利用多余的内存空间。
*/

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* prehead = new ListNode(0);   //这里我们必须要用new，因为这cur是一个pointer，必须要保证是同一个类型，才
        ListNode* cur = prehead;                //能再链子中自由的行走。
        while (l1 != NULL and l2 != NULL){
            if(l1 -> val < l2 -> val){
                cur -> next = l1;
                l1 = l1 -> next;
            }
            else{
                cur -> next = l2;
                l2 = l2 -> next;
            }
            cur = cur->next;    //cur->next是一个ListNode*, 如果你用shared_ptr, 那么cur就是一个shared_ptr
        }                       //等号左边是 shared_ptr,右边是ListNode* ,所以没法用smart ptr啊！！
        cur -> next = l1 == NULL? l2:l1;
        return prehead -> next;
    }
};

//int main (){
//    ListNode* n1 = new ListNode(1);
//    ListNode* n3 = new ListNode(3);
//    ListNode* n5 = new ListNode(5);
//
//    ListNode* n2 = new ListNode(2);
//    ListNode* n4 = new ListNode(4);
//    ListNode* n6 = new ListNode(6);
//
//    (*n1).next = n3;
//    (*n3).next = n5;
//
//    (*n2).next = n4;
//    (*n4).next = n6;
//
//    Solution* s = new Solution;
//    s -> mergeTwoLists(n1, n2);
//}
