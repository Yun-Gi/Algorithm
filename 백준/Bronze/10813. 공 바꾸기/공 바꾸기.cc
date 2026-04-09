#include <iostream>
using namespace std;

int main(){
    int n, m;
    cin>>n>>m;
    int* a = new int[n];//바구니 출력
    for(int i = 0;i<n;i++){
        a[i] = i+1;
    }
    for(int i = 0;i<m;i++){
        int b,c,temp;
        cin>>b>>c;
        temp = a[c-1];
        a[c-1] = a[b-1];
        a[b-1] = temp;
    }
    for(int i = 0; i<n;i++){
        cout<<a[i]<<" ";
    }
    return 0;
}