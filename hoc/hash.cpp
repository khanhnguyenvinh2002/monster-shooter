#include <bits/stdc++.h>
using namespace std;
const int base=1000000007;
long long HA[2000000], HB[2000000],M[2000000];
string a,b;
void buildHash(string s, long long H[]){
    for(int i=1;i<=s.size();i++)
        H[i]=(H[i-1]*43+s[i-1])%base;
}
long long getHash(int L, int R, long long H[]){
    return (H[R]-H[L-1]*M[R-L+1])%base;
}
int main(){
    M[0]=1;
    M[1]=43;
    for(int i=2;i<2000000;i++)
        M[i]=M[i-1]*M[1]%base;
    cin >> a;cin >> b;
    buildHash(a,HA);buildHash(b,HB);
    for (int i=1;i<=a.size()-b.size()+1;i++){
        if (getHash(i,i+b.size()-1,HA)==HB[b.size()]){
            cout << i << " ";}
    }
}

