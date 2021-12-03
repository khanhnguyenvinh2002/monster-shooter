#include <bits/stdc++.h>
using namespace std;

//merge
void merge(int arr[],int l,int m,int r){
    int i=l;//starting index for left subarray
    int j=m+1;//starting index for right subarray
    int k=l;//starting index for temp 
    int size=r-l+1;
    int temp[size];//temporary
    while(i<=m && j<=r){
        if( arr[i]<=arr[j]){
            temp[k]=arr[i];
            i++;
            k++;
        }
        else{
            temp[k]=arr[j];
            j++;
            k++;
        }
    }
    while(i<=m){
        temp[k]=arr[i];//copying elements from left sub
        i++;
        k++;
    }
    while(j<=r){
        temp[k]=arr[j];
        j++;
        k++;
    }
    for(int s=l;s<=r;s++){
        arr[s]=temp[s];
    }
    
}
//merge sort
void mergesort(int arr[],int l, int r){
    if (l<r){
        int m=(l+r)/2;
        mergesort(arr,0,m);
        mergesort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}

int main(){;
    int myarr[10000];
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>myarr[i];
    }
    cout<<"list"<<"\n";
    for(int i=0;i<n;i++){
        cout<<myarr[i]<<" ";
    }
    //merge function
    mergesort(myarr,0,n-1);
    for(int i=0;i<n;i++){
        cout<<myarr[i]<<" ";
    }
}