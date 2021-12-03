#include<bits/stdc++.h>
using namespace std;

const int N=1000000;
int node[4*N];

void update(int id,int l,int r,int i,int val)
{
    if (i<l || i>r) return;
    if(l==r)
    {
        node[id]=val;
        return;
    }
    int mid = (l+r)/2;
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
    return max(query(2*id,l,mid,u,v),query(2*id+1,mid+1,r,u,v));
}

int main()
{
    int n;
    cin>>n;
    for(int i=1;i<=n;i++) 
    {
        cin>>node[i];
        update(1,1,n,i,node[i]);
    }
}
