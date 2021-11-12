#include <iostream>
using namespace std;

int main() {
    int p1, c1, p2, c2;

    cin >> p1 >> c1 >> p2 >> c2;

    if (c1*p1 == c2*p2) {
        cout << "0" << endl;
    } else{
        if (c1*p1 > c2*p2){
            cout << "-1" << endl;
        }
        if (c1*p1 < c2*p2){
            cout << "1";
        }
    }
}
