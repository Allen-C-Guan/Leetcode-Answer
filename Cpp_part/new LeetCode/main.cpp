#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

class Foo {
public:
    int a = 0;
    void PrintFoo () const {
        cout << a << endl;
    }
};



int main() {
    const Foo f1;
    f1.PrintFoo();
    Foo f2;
    f2.PrintFoo();


    std::cout << "Hello, World!" << std::endl;
    return 0;
}
