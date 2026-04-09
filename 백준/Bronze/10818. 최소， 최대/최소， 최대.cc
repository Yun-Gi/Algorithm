#include <iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int *a=new int[n];
    for(int i = 0; i<n; i++){
        cin>>a[i];
    }
    int max = -1000001;
    int min = 1000001;

    for(int i = 0; i<n; i++){
        if(a[i]>max){
            max = a[i];
        }
        if(a[i]<min){
            min = a[i];
        }
    }

    cout<<min<<" "<<max;
    return 0;

}