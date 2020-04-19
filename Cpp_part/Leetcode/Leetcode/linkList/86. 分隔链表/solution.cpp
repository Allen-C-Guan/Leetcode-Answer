#include <iostream>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        if(head == NULL) return NULL;
        ListNode* prehead = new ListNode(-1);
        prehead -> next = head;
        ListNode* fast = prehead -> next, *slow = prehead, *res = prehead, *pre_fast = prehead;
                    //fast要从第二位开始， slow和fast要至少前后错开一位。
        while (fast != NULL) {
            if(fast -> val < x and (slow->next)->val >= x){
                        //是fast在寻找软柿子,而只有在slow后面是大数且fast为小数时，才互换，
                        //不能自己和自己互换是因为链表的特性导致自我互换会有很多问题，因此我们把条件缩小
                pre_fast -> next = fast -> next;
                fast -> next = slow -> next;
                slow -> next = fast;
                slow = slow -> next;       //每次的互换都会带来slow的前进一步
                fast = pre_fast -> next;
            }else{
                if(slow -> next -> val < x) // 要让slow永远停在大数的前面。
                    slow = slow -> next;
                pre_fast = fast;            //fast无论如何也要动
                fast = fast -> next;
            }
        }
        return res -> next;
    }
};

//int main(){
//    ListNode* l1 = new ListNode(1);
//    l1 -> next = new ListNode(2);
//    l1 -> next -> next = new ListNode(5);
//    l1 -> next -> next -> next = new ListNode(2);
//
//    Solution* s = new Solution();
//    s -> partition(l1, 3);
//}
