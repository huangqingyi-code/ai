#include<iostream>
using namespace std;

//��̬��Ա�����ڳ�Ա�����ͳ�Ա����ǰ����Ϲؼ���static
//��̬��Ա����1.���ж�����һ������2.�ڱ���׶η����ڴ�3.���������������ʼ��
//��̬��Ա���������ж�����һ������2.��̬��Ա����ֻ�ܷ��ʾ�̬��Ա����3.Ҳ�з���Ȩ��

//��Ա�����ͳ�Ա�����Ƿֿ��洢�ģ�ֻ�зǾ�̬�ĳ�Ա���������ࣻ��̬����/��̬��Ա����/��Ա��������������
//����ռһ���ֽ�
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
	//p.test();   ���ʷ�ʽһ��ͨ��ʵ����
	//Person::test();  //���ʷ�ʽ��
	cout << Person::a << endl;
	cout << sizeof(Person) << endl;
	system("pause");
	return 0;
}