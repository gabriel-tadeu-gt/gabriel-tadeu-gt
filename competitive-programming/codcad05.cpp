#include <iostream>

using namespace std;

int main(){
    /*
        > 1.8 Alta
        > 1.5 Média
        <= 1.5 Baixa
    */
    double altura;

    cin >> altura;

    if (altura > 1.80){
        cout << "Alta\n";
    } else if (altura > 1.50){
        cout << "Media\n";
    } else if (altura > 1.00){
        cout << "Baixa\n";
    } else {
        cout << "Muito Baixa\n";
    }
}
