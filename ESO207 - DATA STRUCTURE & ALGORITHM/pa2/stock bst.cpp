#include <iostream>
#include <vector>
using namespace std;

class Node{
    public:
    int val;
    Node* left;
    Node*right;
    Node(int x){
        val=x;
        left=NULL;
        right=NULL;
    }
};
Node* insert(int x, Node*root){
    if(root==NULL)return new Node(x);
    if(root->val >=x)root->left=insert(x,root->left);
    else root->right=insert(x,root->right);
    return root;
}
bool search(int x, Node*root){
    if(root==NULL)return false;
    if(root->val == x)return true;
    else if(root->val < x) return search(x,root->right);
    else return search(x,root->left);
}
Node* del(int x, Node*root){
    if(root==NULL)return NULL;
    if(root->val< x) root->right =  del(x,root->right);
    else if(root->val > x)  root->left = del(x,root->left);
    else{
        if(root->left==NULL && root->right==NULL){
            delete root;
            return NULL;
        }
        else if(root->left==NULL){
            Node*temp= root->right;
            delete root;
            return temp;
        }
        else if(root->right==NULL){
            Node*temp= root->left;
            delete root;
            return temp;
        }
        else{
            Node* pred= root->left;
            while(pred->right!=NULL)pred=pred->right;
            int y= pred->val;
            pred->val=x;
            root->val=y;
            root->left= del(x,root->left);
        }
    }
    return root;
}
int main() {
    int d,x;
    char c;
    cin>>d;
    Node* root=NULL;
    for(int i=0;i<d;i++){
        cin>>c>>x;
        if(c=='B') root=insert(x,root);
        else if(c=='S') root=del(x,root);
        else {
            if(search(x,root))cout<<"YES\n";
            else cout<<"NO\n";
        }
    }
    return 0;
}