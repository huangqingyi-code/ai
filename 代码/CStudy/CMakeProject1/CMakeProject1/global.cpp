#include<iostream>
#include<string>
using namespace std;

int a = 3;
int b; //ȫ�ֱ������Բ���ֵ��ϵͳĬ�ϸ�ֵ0

int main()
{
	int c;
	cout << &c << endl;
	cout << ::b << endl;   //��ӡȫ�ֱ���
	{
		int d = 6;
	}
	//cout << d << endl;  ���治�ܵ�������ģ�����Ŀ��Ե��������
	system("pause");
	return 0;
}