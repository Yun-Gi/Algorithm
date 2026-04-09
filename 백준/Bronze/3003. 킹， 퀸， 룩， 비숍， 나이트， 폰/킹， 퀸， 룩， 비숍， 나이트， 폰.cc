#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    int comppiece[6] = {1,1,2,2,2,8};
    int havepiece[6];
    for(int i =0;i<6;i++){
        cin>>havepiece[i];
    }
    for(int i = 0; i<6;i++){
        cout<<comppiece[i] - havepiece[i]<<" ";
    }
    return 0;
}