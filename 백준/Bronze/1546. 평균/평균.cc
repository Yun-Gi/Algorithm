#include <iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    double* arr = new double[n];
    for(int i = 0;i<n;i++){
        cin>>arr[i];
    }

    int max = -1;

    for(int i = 0;i<n;i++){
        if(max<arr[i]){
            max = arr[i];
        }
    }
    double sum =0;
    for(int i = 0;i<n;i++){
        arr[i] = arr[i]/max*100;
        sum += arr[i];
    }
    cout<<sum/n;
    return 0;
}