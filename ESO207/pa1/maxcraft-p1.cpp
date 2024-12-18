#include <iostream>
using namespace std;
int main() {
    int t,n,x;
    cin>>t;
    long long arr[100001];
    while(t--){
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>x;
            arr[i]=x;
        }
        for(int i=n-2;i>=0;i--){
            arr[i]=max(arr[i],arr[i]+arr[i+1]);
        }
        for(int i=0;i<n;i++){
            cout<<arr[i]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}