#include <vector>
#include <iostream>

using namespace std;


 // Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;       //这是ptr，在python里面的绝大部分obj在c里面都是ptr
    TreeNode *right;      //简单理解就是 带有* 的后面的变量就是以ptr形式存放的obj。那么使用的时候就用 -> 就行了。
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> path;
        this -> helper(root, path);
        return path;
    }
    void helper(const TreeNode* root, vector<int>& path){
        if (root == NULL) return;
        this -> helper(root -> left, path);
        path.push_back(root -> val);
        this -> helper(root -> right,path);
    }
    
};
