#include <iostream>
using namespace std;

int main() {
    int num, contador;

    cin >> num;
    contador = 1;
    while (contador <= num){
        if (num % contador == 0) {
            cout << contador << " ";
        }
        contador ++;
    }
}
