#include<bits/stdc++.h>
using namespace std;

void dfs1(int u, int p, vector<vector<int>>&mem, vector<int> &lev, int lo, vector<int> g[]){ 
    mem[u][0] = p; 
    for (int i = 1; i <= lo; i++) 
        mem[u][i] = mem[mem[u][i - 1]][i - 1]; 
    for (int v : g[u]) { 
        if (v != p) 
        { 
            lev[v] = lev[u] + 1; 
            dfs1(v, u, mem, lev, lo, g); 
        } 
    } 
} 
 
int lca(int u, int v, int lo, vector<int> &lev, vector<vector<int>>&mem){ 
    // cout<<u<<" "<<v<<"\n";
    if (lev[u] < lev[v]) swap(u, v); 
    // cout<<lev[u]<<" "<<lev[v]<<"\n";
    for (int i = lo; i >= 0; i--) {
        if ((lev[u] - pow(2, i)) >= lev[v]) 
            u = mem[u][i]; 
        // cout<<u<<" "<<v<<"\n";
    }

    if (u == v) {return u; }

    for (int i = lo; i >= 0; i--){ 
        if (mem[u][i] != mem[v][i]) 
        { 
            u = mem[u][i]; 
            v = mem[v][i]; 
        } 
    } 
    // cout<<"fer";
    return mem[u][0]; 
} 

int dfs(int i, vector<int> g[], vector<int>&a, vector<int>&b, int par ){
    for(auto j: g[i]){
        if(j!=par){
            a[i]+=dfs(j,g,a,b,i);
//             b[i]+=b[j];
        }
    }
    return a[i]-2*b[i];
}

int main(){
    int n,m,x,y,k;
    cin>>n>>k;
    vector<int> g[n],a(n,0),b(n,0); 
    // cout<<n<<" "<<k<<"\n";
    vector<int> a1(n,0),b1(n,0);
    for(int i=0;i<n-1;i++)cin>>a1[i];
    for(int i=0;i<n-1;i++)cin>>b1[i];
    for(int i=0;i<n-1;i++){
        x=a1[i];y=b1[i];
        g[x-1].push_back(y-1);
        g[y-1].push_back(x-1);
    }

    int lo = (int)ceil(log2(n)); 
    vector<vector<int>> mem(n+1,vector<int>(lo+1,-1));
    vector<int> lev(n + 1);
    lev[0]=0;
    dfs1(0, 0, mem, lev, lo, g); 
    // for(int i=0;i<n;i++)cout<<lev[i]<<" ";
    // cout<<"\n";
    for(int i=0;i<k;i++){
        cin>>x>>y;
        int p=lca(x-1,y-1,lo,lev,mem);
//         cout<<x-1<<" "<<y-1<<" "<<p<<"\n";
//         if(x-1!=p)
        a[x-1]++;
//         if(y-1!=p)
        a[y-1]++;
        b[p]+=1;
    }

    dfs(0,g,a,b,-1);
    for(int i=0;i<n;i++)cout<<a[i]-b[i]<<" ";
    return 0;
}