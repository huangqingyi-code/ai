//scope.cpp
//

#include "scope.h"

using namespace std;

int a = 3;//ȫ�ֱ���
int b;//δ��ʾ��ʼ����ȫ�ֱ���

int globle() {
	return 5;
}


void scope_show() {
	cout << a << " " << b << endl; //��ӡȫ�ֱ���a��b

	int c = 0; //����ֲ�����c,�ֲ����������ʼ��
	int a = 2; //����ֲ�����a,�ֲ����������ʼ��

	cout << c << " " << a << endl; //��ӡ�ֲ�����c��a

	cout << a<< " " << ::a << endl;//��ӡ�ֲ�����a��ȫ�ֱ���a

	{
		int d = 5; //������б���d
	}
	//cout << d << endl; //��ͼ��ӡ��d

	cout << ::globle() << endl; //����ȫ�ֺ���
}
