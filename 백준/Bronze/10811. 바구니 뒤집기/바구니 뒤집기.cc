#include <iostream>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int* a=new int[n];
   
    for(int i=0;i<n;i++){
        a[i] = i+1;
    }
    for(int i=0;i<m;i++){
        int q,w;
        cin>>q>>w;
        for(int i=0;i<(w-q+1)/2;i++){
            int temp = a[w-i-1];
            a[w-i-1] = a[q+i-1];
            a[q+i-1] = temp; 
        }
    }
    for(int i = 0;i<n;i++){
        cout<<a[i]<<" ";
    }
    return 0;
}