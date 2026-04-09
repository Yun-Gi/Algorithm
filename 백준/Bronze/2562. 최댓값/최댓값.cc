#include <iostream>
using namespace std;

int main(){
    int a[9];
    int max = 0;
    int n;

    for(int i = 0; i<9; i++){
       cin>>a[i];
    }
    for(int i = 0; i<9; i++){
        if(max<a[i]){
            max = a[i];
            n = i;
        }
    }

    cout<<max<<"\n"<<n+1<<endl;
    return 0;
}