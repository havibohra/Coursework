#include<iostream>
using namespace std;
long long mod=998244353;

void mutliplier(long long** mat1, long long** mat2, int k){
    long long** temp = new long long*[k];
    for(int i=0;i<k;i++){
        temp[i]= new long long[k];
    }
    for(int i=0;i<k;i++){
        for(int j=0;j<k;j++){
            temp[i][j]=0;
            for(int p=0;p<k;p++){
                temp[i][j]= (temp[i][j]+ ((mat1[i][p]%mod)*(mat2[p][j]%mod))%mod)%mod;
            }
        }
    }

    for(int i=0;i<k;i++){
        for(int j=0;j<k;j++){
            mat1[i][j] = temp[i][j];
        }
    }
    for(int i=0;i<k;i++) delete []temp[i];
    delete []temp;
    return;
}

void power(long long k,long long** mat, long long n, long long** POV){
    if(n==1){
        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                POV[i][j] = mat[i][j];
            }
        }
        return;
    }
    long long** temp = new long long*[k];
    for(int i=0;i<k;i++){
        temp[i]= new long long[k];
    }
    power(k,mat,n/2,temp);
    mutliplier(temp,temp,k);
    if(n%2)mutliplier(temp,mat,k);
    for(int i=0;i<k;i++){
        for(int j=0;j<k;j++){
            POV[i][j] = temp[i][j];
        }
    }
    for(int i=0;i<k;i++) delete []temp[i];
    delete []temp;
    return;
}

void solve(long long n, long long k){
    if(n==1){cout<<1<<"\n";return;}
    if(n<=k){
        // long long ans=1;
        long long arr[n+1]= {0};
        arr[1]=1;
        for(int i=2;i<=n;i++){
            for(int j=1;j<i;j++){
                arr[i]+=arr[j];
            }
            arr[i]+=1;
            arr[i]%=mod;
        }
        cout<<arr[n]%mod<<"\n";
        return;
    }
    else{
        long long arr[k+1]= {0};
        arr[1]=1;
        for(int i=2;i<=k;i++){
            for(int j=1;j<i;j++){
                arr[i]+=arr[j];
            }
            arr[i]+=1;
            arr[i]%=mod;
            // cout<<arr[i]<<" ";
        }

        long long** mat = new long long*[k];
        long long** POV = new long long*[k];
        for(int i=0;i<k;i++){
            mat[i]= new long long[k];
            POV[i]= new long long[k];
        }

        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                if(i==0 || i==j+1)mat[i][j]=1;
                else mat[i][j]=0;
            }
        }

        power(k,mat,n-k,POV);
        long long ans=0;
        // for(int i=0;i<k;i++){
        //     for(int j=0;j<k;j++){
        //         cout<<POV[i][j]<<" ";
        //     }
        //     cout<<"\n";
        // }
        for(int i=0;i<k;i++){
            ans+= (POV[0][i]*arr[k-i])%mod;
            ans%=mod;
        }

        for(int i=0;i<k;i++) {
            delete []mat[i];
            delete []POV[i];
        }
        delete []mat;
        delete []POV;
        cout<<ans<<"\n";
    }
}
int main(){
    int t;
    long long n,k;
    cin>>t;
    while(t--){
        cin>>n>>k;
        solve(n,k);
    }
}