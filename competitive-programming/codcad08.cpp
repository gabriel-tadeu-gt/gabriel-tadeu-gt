#include <iostream>
using namespace std;

int main(){
    int x;

    for (x = 1; x <= 5; x++) {
        if (x == 2) {
            continue;
        }
        cout << x << endl;

    }
}
