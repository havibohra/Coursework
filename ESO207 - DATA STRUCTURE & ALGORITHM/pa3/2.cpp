#include<bits/stdc++.h>
using namespace std;

void dfs(int i, vector<int>&vis, vector<int>&dfn, vector<int>&low, int par, vector<int> g[], int &d, vector<int>&cycle){
    // cout<<"#"<<i<<" ";
    dfn[i]=d;
    low[i]=d;
    vis[i]=1;
    for(auto j: g[i]){
        if(j!=par){
            if(vis[j]){
                low[i] = min(low[i],dfn[j]);
            }
            else{
                d++;
                dfs(j,vis,dfn,low,i,g,d,cycle);
                low[i] = min(low[i],low[j]);

                if(low[j] <= dfn[i]){
                    // cout<<i<<" "<<j<<"\n";
                    // cout<<dfn[i]<<" "<<low[j]<<"\n";
                    cycle[i]=1;
                    cycle[j]=1;
                }
            }
        }
    }
}

int main(){
    int n,m,x,y;
    cin>>n>>m;
    vector<int> a(m),b(m);
    vector<int> g[n];
    for(int i=0;i<m;i++)cin>>a[i];
    for(int i=0;i<m;i++)cin>>b[i];
    for(int i=0;i<m;i++){
         x=a[i];y=b[i];
        // cout<<x<<" "<<y<<"\n";
        g[x-1].push_back(y-1);
        g[y-1].push_back(x-1);
    }
    vector<int> vis(n,0), dfn(n,-1), low(n,-1),cycle(n,0);
    for(int i=0;i<n;i++){
        if(vis[i])continue;
        int d=0;
        dfs(i,vis,dfn,low,-1,g,d,cycle);
    }
    for(int i=0;i<n;i++){
        cout<<cycle[i]<<" ";
    }
    // cout<<"\n";
    // for(int i=0;i<n;i++){
    //     cout<<dfn[i]<<" ";
    // }
    // cout<<"\n";
    // for(int i=0;i<n;i++){
    //     cout<<low[i]<<" ";
    // }
    return 0;
}