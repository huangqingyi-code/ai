#include<iostream>
using namespace std;
//1.解决名称冲突2.返回对象本身*this
//
class Person
{
public:
	int m_age;
	Person(int age)
	{
		m_age = age;   //this->解决名称冲突
	}
	Person& personaddage(Person& p)    //Person personaddage(Person& p) 返回的是Person的值，不是对象
	{
		m_age += p.m_age;
		return *this;
	}
};

int main()
{
	Person p1(10);
	Person p2(20);
	p2.personaddage(p1).personaddage(p1);  //链式编程，返回p2
	cout << p2.m_age << endl;
	system("pause");
	return 0;
}