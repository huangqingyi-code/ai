#include<iostream>
using namespace std;
//1.������Ƴ�ͻ2.���ض�����*this
//
class Person
{
public:
	int m_age;
	Person(int age)
	{
		m_age = age;   //this->������Ƴ�ͻ
	}
	Person& personaddage(Person& p)    //Person personaddage(Person& p) ���ص���Person��ֵ�����Ƕ���
	{
		m_age += p.m_age;
		return *this;
	}
};

int main()
{
	Person p1(10);
	Person p2(20);
	p2.personaddage(p1).personaddage(p1);  //��ʽ��̣�����p2
	cout << p2.m_age << endl;
	system("pause");
	return 0;
}