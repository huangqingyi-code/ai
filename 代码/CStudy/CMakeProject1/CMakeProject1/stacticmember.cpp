#include<iostream>
using namespace std;

//静态成员就是在成员变量和成员函数前面加上关键字static
//静态成员变量1.所有对象共享一份数据2.在编译阶段分配内存3.类内声明，类外初始化
//静态成员函数：所有对象共享一个函数2.静态成员函数只能访问静态成员变量3.也有访问权限

//成员变量和成员函数是分开存储的，只有非静态的成员变量属于类；静态变量/静态成员函数/成员函数都不属于类
//空类占一个字节
class Person
{
public:
	int b;
	static int a;
	static void test()
	{
		a = 30;
		cout << "static call" << endl;
	}
	void test01()
	{
		cout << "hello python" << endl;
	}
};
int Person::a = 0;
int main()
{
	Person p;  
	//p.test();   访问方式一：通过实例化
	//Person::test();  //访问方式二
	cout << Person::a << endl;
	cout << sizeof(Person) << endl;
	system("pause");
	return 0;
}