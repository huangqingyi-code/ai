#include<iostream>
using namespace std;
#include<string>
//��Ԫ��1.ȫ�ֺ�������Ԫ2.������Ԫ��һ������Է�����һ�����˽�г�Ա3.��Ա��������Ԫ������������е�˽�г�Ա
class Person
{
	friend void goodfriend(Person *p);   //ȫ�ֺ�������˽�б���
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