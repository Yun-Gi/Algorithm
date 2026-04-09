#include <iostream>
using namespace std;

int main(){
    int n, m;
    cin>>n>>m;
    int* a = new int[n];//바구니 출력
    for(int i = 0;i<n;i++){
        a[i] = 0;
    }
    for(int i = 0;i<m;i++){
        int u,j,k;
        cin>>u>>j>>k;
        for(int g=u-1;g<j;g++){
            a[g] = k;
        }
    }
    for(int i = 0; i<n;i++){
        cout<<a[i]<<" ";
    }
    return 0;
}