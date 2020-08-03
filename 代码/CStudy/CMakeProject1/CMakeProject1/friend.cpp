#include<iostream>
using namespace std;
#include<string>
//友元：1.全局函数做友元2.类做友元，一个类可以访问另一个类的私有成员3.成员函数做友元，类外访问类中的私有成员
class Person
{
	friend void goodfriend(Person *p);   //全局函数访问私有变量
public:
	string car;
	Person()
	{
		car = "aodi";
		psw = 123456;
	}
private:
	int psw;
};
void goodfriend(Person *p)
{
	cout << "frien is looking your car: " << p->psw << endl;
}
int main()
{
	Person wusir;
	goodfriend(&wusir);
	system("pause");
	return 0;
}