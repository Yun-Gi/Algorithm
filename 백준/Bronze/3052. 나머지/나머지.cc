#include <iostream>
using namespace std;

int main(){
    int a[10],b[42];
    for(int i=0;i<42;i++){
        b[i] = 0;
    }
    for(int i=0;i<10;i++){
        cin>>a[i];
    }
    for(int i=0;i<10;i++){
        int c=a[i] % 42;
        b[c]++;
    }
    int sum = 0;
    for(int i=0;i<42;i++){
        if(b[i]!=0){
            sum++;
        }
    }
    cout<<sum;
    return 0;
}