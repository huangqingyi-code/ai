#include<iostream>
using namespace std;

class Person
{
public:
	int a;
	mutable int b;
	void test01() const    //�������ڲ������޸ĳ�Ա���ԣ�ֻ���޸�mutable���ε�
		                   //����const֮�� const Person *const this
	{
		b = 10;
	}
	void test02()
	{
		a = 10;
		//this = NULL;    // thisָ�뱾������һ��ָ�볣����ָ���ָ���ǲ������޸�,ָ��ʵ�����Ķ��󣬲����޸�ָ��ָ��
	}
};
int main()
{
	const Person p;   //������ֻ�ܵ��ó�����
	p.test02();

}