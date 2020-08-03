#include<iostreanm>
using namespace std;
//一函数默认参数：1.声明函数和实现函数只能一个由默认参数2.默认参数放最后面



//二函数占位参数，用来占位，调用时必须填补
//void func(int a,int)   //第二占位

//函数重载：函数名可以相同，提高复用性
//函数重载条件：1.同一个作用域2.函数名相同3.函数参数类型不同或者个数或者顺序不同4.只是返回值不同不可以重载
//void func()
//{
//	cout << "调用了func" << endl;
//}
//void func(int a) {
//	cout << "调用了func(int a)" << endl;
//}
//void func(int a,int b) {
//
//}

//1.函数重载的注意事项：引用作为重载条件时，根据调用输入不同的值调用不同函数
void func(int &a)  //func(x)   int &a = 10 不合法
void func(const int &a)   //func(10)
//2.函数重载遇到默认参数：会报错

