#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m,x,y;
    cin>>n>>m;
    vector<int> g[n];
    for(int i=0;i<m;i++){
        cin>>x>>y;
        g[x-1].push_back(y-1);
        g[y-1].push_back(x-1);
    }
    bool flag=false;
    vector<int> depth(n,-1);
    queue<int> q;
    for(int i=0;i<n;i++){
        if(depth[i]!=-1)continue;
        q.push(i);
        depth[i]=0;
        while(!q.empty()){
            int p= q.front();
            q.pop();
    
            for(auto j: g[p]){
                if(depth[j]==-1){
                    depth[j]=depth[p]+1;
                    q.push(j);
                }
                else if(depth[j]==depth[p]){flag=true;}
            }
        }
    }
    if(flag)cout<<"NO";
    else {
        cout<<"YES\n";
        for (int i = 0; i <n; ++i)
        {
            cout<<depth[i]%2+1<<" ";
        }
    }
    return 0;
}