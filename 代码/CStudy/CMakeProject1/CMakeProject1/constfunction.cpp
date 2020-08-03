#include<iostream>
using namespace std;

class Person
{
public:
	int a;
	mutable int b;
	void test01() const    //常函数内不可以修改成员属性，只能修改mutable修饰的
		                   //加了const之后 const Person *const this
	{
		b = 10;
	}
	void test02()
	{
		a = 10;
		//this = NULL;    // this指针本质上是一个指针常量，指针的指向是不可以修改,指向实例化的对象，不能修改指针指向
	}
};
int main()
{
	const Person p;   //常对象只能调用常函数
	p.test02();

}