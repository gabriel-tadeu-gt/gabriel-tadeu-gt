#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int qtd;
    double num;

    cout.precision(4);
    cout.setf(ios::fixed);

    cin >> qtd;

    for (int i = 0; i < qtd; i++) {
        cin >> num;
        cout << sqrt(num) << endl;
    }
}
