#include <iostream>
#include <vector>
using namespace std;

long long int merge(vector<int> &v,int s,int mid,int e){
    if(s>=e)return 0;
    long long int ans=0;
    auto left  =new int[mid-s+1];
    auto right =new int[e-mid];

    int k=s;
    for(int i=0;i<mid-s+1;i++) left[i]=v[k++];
    for(int i=0;i<e-mid;i++) right[i]=v[k++];
    int i=0,j=0, len1=mid-s+1, len2=e-mid;

    int index=s;
    while(i<len1 && j<len2){
        if(left[i]<=right[j]){
         v[index++]=left[i++];
        }
        else{
         ans+=(len1-i);
         v[index++]=right[j++];
        }
    }
    while(i<len1) v[index++]=left[i++];
    while(j<len2) v[index++]=right[j++];
    delete []left;
    delete []right;
    return ans;
}
long long int mergesort(vector<int> &v,int s,int e){
    if(s>=e)return 0;
    int mid= s + (e-s)/2;
    long long int ans=0;
    ans+=mergesort(v,s,mid);
    ans+=mergesort(v,mid+1,e);
    ans+=merge(v,s,mid,e);
    return ans;
}

int main() {
    int t,n;
    cin>>t;
    while(t--){
        cin>>n;
        vector<int> v;
        for(int i=0;i<n;i++){
            int x; cin>>x;
            v.push_back(x);
        }
        cout<<mergesort(v,0,n-1)<<"\n";
    }
    return 0;
}