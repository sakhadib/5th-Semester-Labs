#include <iostream>
#include <type_traits>
using namespace std;

template <typename T>
void func(T value) {
    if (is_same<T,int>::value){
        cout<<value<<endl;
    }
    else {
        cout<<"Invalid Type"<<endl;
    }
}

int main() {
    
    int i = 10;
    double d = 25.98;
    
    func(i);
    func(d);
    
    return 0;
}