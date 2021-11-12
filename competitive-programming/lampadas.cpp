#include <iostream>
using namespace std;

int main(){
    int n, lamp1, lamp2, estado;
    cin >> n;
    lamp1 = lamp2 = 0;

    for (int i = 0; i < n; i++){
        cin >> estado;
        if (estado == 1){
            lamp1 = 1 - lamp1;
        } else if (estado == 2){
            lamp1 = 1 - lamp1;
            lamp2 = 1 - lamp2;
        }
    }

    cout << lamp1 << endl << lamp2 << endl;
}
