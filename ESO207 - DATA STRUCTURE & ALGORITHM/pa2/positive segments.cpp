#include <iostream>
#include <vector>
using namespace std;

void solver(vector<int>&v, int i, int j, vector<int>&depth, int h){
    if(j<0 ||i>=v.size())return;
    int maxi=-1, ind=-1;
    for(int p=i;p<=j;p++){
        if(v[p]>maxi){
            maxi=v[p];
            ind=p;
        }
    }
    depth[ind]=h;
    solver(v,i,ind-1,depth,h+1);
    solver(v,ind+1,j,depth,h+1);
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> v(n);
        for(int i=0;i<n;i++)cin>>v[i];
        vector<int> depth(n,0);
        solver(v,0,n-1,depth,0);
        for(auto j:depth)cout<<j<<" ";
        cout<<"\n";
    }
}