#include <bits/stdc++.h>
using namespace std;
int N=1000000;
int node[4*N];
int lazy[4*N];

void down(int id)
{
    int t= lazy[id];
    lazy[2*id]+=t;
    lazy[2*id+1]+=t;
    node[2*id+1]+=t;
    node[2*id]+=t;
    lazy[id]=0;
}
void update(int id,int l,int r,int u, int v, int k)
{
    if (v<l || u>r) return;
    if(u<=l && r<=v)
    {
        node[id]+=k;
        lazy[id]+=k;
        return;
    }
    int mid = (l+r)/2;
    down(id);
    update(2*id,l,mid,i,val);
    update(2*id+1,mid+1,r,i,val);
    node[id]=min(node[2*id],node[2*id+1]);
    return;
}

int query(int id,int l,int r,int u,int v)
{
    if(u>r || v<l) return 1000000000;
    if(u<=l && r<=v) return node[id];
    int mid = (l+r)/2;
    down(id);
    return max(query(2*id,l,mid,u,v),query(2*id+1,mid+1,r,u,v));
}

int main(){
    int n,m;
    cin>>n>>m;
    for (int i=0;i<m;i++){
        int a,b,c,d;
        cin>>a;
        if (a==0){
            cin>>b>>c>>d;
            update(1,1,n,b,c,d);
        }
        if (a==1){
            cin>>b>>c;
            int ans;
            ans=query(1,1,n,b,c);
            cout<<ans;
        }
    }
}