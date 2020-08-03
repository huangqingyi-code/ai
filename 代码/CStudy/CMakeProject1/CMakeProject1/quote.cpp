#include<iostream>
using namespace std;
//引用,给变量起别名
//注意事项：1.引用必须要初始化：int &b = a，不能int &b；
//2：引用一旦初始化后不能更改int &b = a，后面不能int &b = c；b=c是赋值不是引用
//int main()
//{
//	int a = 10;
//	int &b = a;
//	cout << &a <<" " <<&b << endl;
//	system("pause");
//	return 0;
//}

//函数中引用传递,也会改变值
//void swap(int &a, int &b)
//{
//	int temp = a;
//	a = b;
//	b = temp;
//}
//int main()
//{
//	int a = 10;
//	int b = 20;
//	swap(a, b);
//	cout << a << b << endl;
//	system("pause");
//	return 0;
//}

//引用做函数的返回值；1.不要返回局部变量的引用；2.函数的调用可以作为左值
/*
int &func()   //返回一个引用
{
	static int a = 10;
	return a;
}
int main()
{
	int &ret = func();
	cout << ret << endl;    //10
	func() = 60;   //返回的引用被修改，ret也随之被更改
	cout << ret << endl;    //60
	system("pause");
	return 0;
}
*/

//引用的本质：在c++内部实现了一个指针常量
// int &ret = a,自动转化成 int *const ret = &a
//ret = 20,实际上是 *ret = 20

//常量引用：主要用来修饰形参，防止误操作。本来这样int &a = 10是不可以的，加上const就可以
//const int &a = 10,其实是 temp = 10  int & a = temp(编译器帮你做了这一步)

void show(const int &ret)
{
	//ret = 10;   不能修改,修改的话传入该函数的值也会被修改（main函数中的a）,但是在主函数内部可以修改
	cout << ret << endl;
}
int main()
{
	int a = 10;
	show(a);
	a = 20;
	cout << a << endl;
	system("pause");
	return 0;
}