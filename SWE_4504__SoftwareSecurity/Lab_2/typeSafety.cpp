#include <iostream>
using namespace std;

class Duck {
    bool rubber;
    public:
    // TODO : Added a destructor to make the class polymorphic
    virtual ~Duck() {}
    void setRubber(bool value){
        rubber = value;
    }
    void quack(){
        if(rubber)cout<<"Artificial Quack"<<'\n';
        else cout<<"Real Quack"<<'\n';
    }
};

class RubberDuck: public Duck{
    public:
    RubberDuck(){
        setRubber(true); // ! Setting as rubber
    }
};

class RealDuck: public Duck{
    public:
    RealDuck(){
        setRubber(false); // ! Setting as non-rubber
    }
};

template <typename T>
void processData(T value) {
    if constexpr(is_same<T,int>::value){
        cout<< "Int : "<< value << endl;
    }
    else if(is_same<T,double>::value){
        cout<< "Double : "<< value << endl;
    }
    else {
        cout<<"Invalid Type"<<endl;
    }
}

int main() {
    int i = 42;
    double d = 3.14;

    // TODO : Pass correct type value (1 for integer) .. Passing value istead of pointer
    processData(i);
    
    Duck *d1 = new RubberDuck();
    Duck *d2 = new RealDuck();

    // TODO : Use dynamic_cast to ensure proper runtime type safety
    RealDuck *rd = dynamic_cast<RealDuck*>(d1);
    
    if(rd){
        rd->quack();
    }
    else {
        cout<<"Casting Error"<<'\n';
    }

    // TODO : Free memory
    delete d1;
    delete d2;

    return 0;
}
