#include <iostream>
using namespace std;

int main(){
    int n,v;
    int s = 0;
    cin>>n;
    int a[n];

    for(int i = 0; i<n;i++){
        cin>>a[i];
    }
    cin>>v;
    for(int i = 0; i<n;i++){
        if(a[i]==v){
            s++;
        }
    }
    cout<<s;
    return 0;

}