/*stack<int>s;
s.push(x) thêm vào
s.top() xóa phần tử cuối cùng
s.size() kích thước
stack<kieu du lieu>tenstack

queue<int> q;
q.top()phan tu dau tien them vao
q.back()phan tu cuoi cung them vao
q.size()

stack<string>s;
1234=>'1234'
ép từ string về int:


stack<int> mystack;
mystack.push(10);
mystack.push(20);
mystack.top()20*/
#include <bits/stdc++.h>
int main(){
    stack<string>s;
    s.push("1234");
    s.push("123");
    while(s.size()>0){
        stringstream ss;
        int num=0;
        ss << s.top();
        ss>>num;
        cout<<num<<" ";
        s.pop()
    }
//cplusplus.com//

}