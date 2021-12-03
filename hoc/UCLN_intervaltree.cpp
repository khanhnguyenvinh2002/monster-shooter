#include <bits/stdc++.h>
using namespace std;
const int N=1000000;
int node[4*N];
void update(int id,int l, int r, int i, int val){
    if (i<l||i>r) return;
    if(l==r){
        node[id]=val;
        return;
    }
    int mid=(l+r)/2;
    update(2*id,l,mid,i,val);
    update(2*id+1,mid+1,r,i,val);
    node[id]=__gcd(node[2*id],node[2*id+1]);
    return;
}

int query(int id,int l, int r, int u, int v){
    if(u>r||v<l) return 100000000000;
    if (u<=l && r<=v) return node[id];
    int mid=(l+r)/2;
    return __gcd(query(2*id,l,mid,u,v),query(2*id+1,mid+1,r,u,v));
}
int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>node[i];
    }
    for(int i=1;i<=n;i++){
        cout<<node[i]<<" ";}
    int m;
    cin>>m;
    for (int i=0;i<m;i++){
        int x,l,r;
        cin>> x>>l>>r;
        if (x==1){
            node[r]=l;
            for(int i=1;i<=n;i++){
                cout<<node[i]<<" ";
            }
        }
        if (x==2){
            int ucln=query(1,1,n,l,r);
            cout<<ucln;
        }
    }
}
