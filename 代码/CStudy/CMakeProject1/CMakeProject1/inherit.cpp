#include<iostream>
using namespace std;
//公有继承：原先公有的还是公有，保护的还是保护
//保护继承：原先公有的和保护的都变成保护
//私有继承：原先公有的和保护的变成私有的

//在父类中非静态的成员属性都会被继承，父类中私有的成员的成员属性被编译器隐藏了访问不到，但还是被继承了。
//继承中构造和析构的顺序：继承中先调用父类构造函数再调用子类构造函数，先调用子类析构再调用父类析构（栈区先进后出）

//当子类中有跟父类同名的成员和函数时，默认调用子类，要想调用父类的要加作用域Base::

//子类继承多个父类和菱形继承先学

//class Basepage
//{
//public:
//	void header() {
//		cout << "欢迎登陆" << endl;
//	}
//	void fooder() {
//		cout << "帮助中心" << endl;
//	}
//	void left() {
//		cout << "导航栏" << endl;
//	}
//};
//class Python :public Basepage
//{
//public:
//	void content() {
//		cout << "pthon学科视频" << endl;
//	}
//};
//class Java :public Basepage
//{
//public:
//	void content() {
//		cout << "java视频学科"<<endl;
//	}
//};
//void test() {
//	Python p;
//	p.header();
//	p.fooder();
//	p.left();
//	p.content();
//	Java j;
//	j.header();
//	j.fooder();
//	j.left();
//	j.content();
//}
//int main() {
//	test();
//	system("pause");
//	return 0;
//}

class Base
{
public:
	int m_a;
	Base()
	{
		m_a = 100;
	}
	void func() {
		cout << "base func()" << endl;
	}
};
class Son :public Base
{
public:
	int m_a;
	Son()
	{
		m_a = 200;
	}
	void func()
	{
		cout << "son func()" << endl;
	}
};
int c = 6;
int main()
{
	Son s;
	cout << s.m_a << endl;
	cout << s.Base::m_a << endl;
	system("pause");
	return 0;
}