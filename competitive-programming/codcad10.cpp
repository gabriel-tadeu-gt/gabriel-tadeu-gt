#include <iostream>
using namespace std;

int main(){
    int v[5];
    int i;

    for (i = 0; i < 5; i++){
        cin >> v[i];
    }

    for(i = 4; i >= 0; i--){
        cout << v[i] << " ";
        if (i == 0){
            cout << endl;
        }
    }

}
