#include<iostream>
using namespace std;
bool pos(int mid, int* arr, int n, long long k){
	long long sum=0;
	for(int i=0;i<n;i++){
		if(arr[i]>mid){
			sum+= 1LL*arr[i]*(arr[i]+1)/2;
			sum-= 1LL*mid*(mid+1)/2;1	
			if(sum>k)return false;
		}
	}
	return true;
}
int solve(int* arr, int n, long long k ){
	int lo=0,hi=1e6+1,mid,ans;
	while(lo<=hi){
		mid= (lo+hi)>>1;
		if(pos(mid,arr,n,k)){
			ans=mid;
			hi=mid-1;
		}
		else lo=mid+1;
	}
	return ans;
}
int main(){
	int t,n,x;
	long long k;
	cin>>t;
	int arr[100001];
	while(t--){
		cin>>n>>k;
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		cout<<solve(arr,n,k)<<"\n";
	}
}