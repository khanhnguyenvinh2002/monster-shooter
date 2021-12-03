#include <bits/stdc++.h>
using namespace std;

long long A[100000];
long long M[400];
int sq_n = 330;
int blockOfM( int i){
    return b[i];
}
int duyetLR(int l, int r){
    int bl=blockOfM(l);
    int br=blockOfM(r);
    if (blockOfM(l)==blockOfM(r)){
        int x=20000000000;
            for (int i=l;i<r+1;i++){
                if (A[i]<x){
                    x=A[i];
                }
            }
            return x;
    }
    else{
        int minlr =20000000000;
            for (int i=l; i<bl*sq_n+sq_n; i++){
                if (A[i]<minlr){
                    minlr=A[i];
                }
            }
            for (int i=bl+1;i<br;i++){
                if (M[i]<minlr){
                    minlr=M[i];
                }
            }
            for (int i=br*sq_n;i<r+1;i++){
                if (A[i]<minlr){
                    minlr=A[i];
                }
            }
            return minlr;


    }
    
}
int main(){
    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        cin>>A[i];
    }
    for (int i=0;i<sq_n;i++){
        M[i]=200000000;
        for (int j=i*sq_n;j<min(n,i*sq_n+sq_n);j++){
            b[j]=i;
            if (A[j]<M[i]){
                M[i]=A[j];
            }
        }
    }
    cin>>m;
    for (int i=0;i<m;i++){
        int x,l,r;
        cin>> x>>l>>r;
        if (x==1){
            A[l]=r;
            M[blockOfM(l)]=min(M[blockOfM(l)],r);
        }
        if (x==2){
            int minn=duyetLR(l,r);
            cout<<minn;
        }
    }
}