#include <iostream>
#include <vector>
using namespace std;

int main(){
    int A[9][9];
    int lar = -1,x,y;

    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cin>>A[i][j];
        }
    }

    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            if(lar<A[i][j]){
                lar = A[i][j];
                x = i;
                y = j;
            }
        }
    }

    cout<<lar<<endl<<x+1<<" "<<y+1;
    return 0;
}