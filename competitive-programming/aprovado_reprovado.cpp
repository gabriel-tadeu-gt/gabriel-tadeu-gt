#include <iostream>
using namespace std;

int main(){
    double n1, n2, media;
	
    cin >> n1 >> n2;

    media = (n1 + n2) / 2;

    if (media >= 7) {
        cout << "Aprovado\n";
    } else if (media >= 4){
        cout << "Recuperacao\n";
    } else {
        cout << "Reprovado\n";
    }
}
