#include <iostream>
#include <vector>
using namespace std;

bool Poss(vector<int> &a,vector<int> &l,vector<int> &r, int k,int mid, vector<int> &p){
	vector<int> temp=a;

	for(int i=0;i<mid;i++) 
		if(temp[p[i]-1]<0) 
			temp[p[i]-1]= -temp[p[i]-1];
	for(int i=1;i<temp.size();i++) temp[i]+=temp[i-1];
	int count=0;
	for(int i=0;i<l.size();i++){
		int sum=temp[r[i]-1];
		if(l[i]-1>0) sum-= temp[l[i]-2];
		if(sum>0) count++;
	}
	// cout<<count<<"\n";
	return count>=k;
}

int main(){
	int t;
	cin>>t;
	while(t--){
		int n,s;
		cin>>n>>s;
		vector<int> a(n);
		for(int i=0;i<n;i++)cin>>a[i];
		vector<int> l(s);
		vector<int> r(s);
		for(int i=0;i<s;i++)cin>>l[i]>>r[i];
		int q,k;
		cin>>q>>k;
		vector<int> p(q);
		for(int i=0;i<q;i++)cin>>p[i];

		int lo=0,hi=q;
		int mid=(lo+hi)>>1;
		int ans=-1;
		while(lo<=hi){
			if(Poss(a,l,r,k,mid,p)){
				ans=mid;
				// cout<<ans<<" ";
				hi=mid-1;
			}
			else lo=mid+1;
			mid=(lo+hi)>>1;
		}
		cout<<ans<<"\n";
	}
}