#include <bits/stdc++.h>
using namespace std;
int main(){   
int n;
long long a[10000000];
long long f[10000000];
int kq=-1;
    cin>>n;
    for (int i=1;i<=n;i++){cin>>a[i];}
    for (int i=1;i<=n;i++){
        f[i]=1;
        for (int j=1;j<i;j++){
            if(a[j]<a[i]){
                f[i]=max(f[i],f[j]+1LL);
            }
        }
    }
    for (int i=1;i<=n;i++){
        if (f[i]>kq){
            kq=f[i];
        }
    }
    cout<<kq;
    system("pause");
    return 0;
}
