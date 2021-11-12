#include <iostream>
using namespace std;

int main(){
    int alunos, monitores, total;

    cin >> alunos >> monitores;

    total = alunos + monitores;

    if (total <= 50){
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }

}
