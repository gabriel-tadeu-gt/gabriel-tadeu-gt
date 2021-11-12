#include <iostream>
using namespace std;

/* */
//
int main() {
    /*

    */

    int x;

    cin >> x;

    if (x >= 0 and x % 2 == 0){
        cout << "x positivo e par\n";
    } else {

        if (x <=0 ){
            cout << "x nao positivo \n";
        }

        if (x % 2 != 0) {
            cout << "x nao eh par \n";
        }
    }

}
