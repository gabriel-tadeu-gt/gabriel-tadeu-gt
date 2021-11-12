#include <iostream>
using namespace std;

int main() {
    int n, i, latas, copos, quebrados;
    cin >> n;
    i = 0;
    quebrados = 0;
    while (i < n){
        cin >> latas >> copos;
        if (latas > copos){
            quebrados += copos;
        }
        i++;
    }

    cout << quebrados << endl;

}
