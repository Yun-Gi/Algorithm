#include <iostream>
using namespace std;

int main(){
    int n,x;
    int s = 0;
    cin>>n>>x;
    int* a = new int[n];
    for(int i = 0; i < n; i++){
        cin>>a[i];
    }
    for(int i=0; i<n; i++){
        if(a[i]<x){
            s++;
        }
    }
    int l = 0;
    int* a1 =new int[s];
    for(int i = 0; i<n;i++){
        if(a[i]<x){
            a1[l++] = a[i];
        }
    }
    for(int i = 0; i<s;i++){
        cout<<a1[i]<<" ";
    }
    delete[] a;
    delete[] a1;

    return 0;
}