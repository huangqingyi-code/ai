#include<iostream>
using namespace std;
//����,�����������
//ע�����1.���ñ���Ҫ��ʼ����int &b = a������int &b��
//2������һ����ʼ�����ܸ���int &b = a�����治��int &b = c��b=c�Ǹ�ֵ��������
//int main()
//{
//	int a = 10;
//	int &b = a;
//	cout << &a <<" " <<&b << endl;
//	system("pause");
//	return 0;
//}

//���������ô���,Ҳ��ı�ֵ
//void swap(int &a, int &b)
//{
//	int temp = a;
//	a = b;
//	b = temp;
//}
//int main()
//{
//	int a = 10;
//	int b = 20;
//	swap(a, b);
//	cout << a << b << endl;
//	system("pause");
//	return 0;
//}

//�����������ķ���ֵ��1.��Ҫ���ؾֲ����������ã�2.�����ĵ��ÿ�����Ϊ��ֵ
/*
int &func()   //����һ������
{
	static int a = 10;
	return a;
}
int main()
{
	int &ret = func();
	cout << ret << endl;    //10
	func() = 60;   //���ص����ñ��޸ģ�retҲ��֮������
	cout << ret << endl;    //60
	system("pause");
	return 0;
}
*/

//���õı��ʣ���c++�ڲ�ʵ����һ��ָ�볣��
// int &ret = a,�Զ�ת���� int *const ret = &a
//ret = 20,ʵ������ *ret = 20

//�������ã���Ҫ���������βΣ���ֹ���������������int &a = 10�ǲ����Եģ�����const�Ϳ���
//const int &a = 10,��ʵ�� temp = 10  int & a = temp(����������������һ��)

void show(const int &ret)
{
	//ret = 10;   �����޸�,�޸ĵĻ�����ú�����ֵҲ�ᱻ�޸ģ�main�����е�a��,�������������ڲ������޸�
	cout << ret << endl;
}
int main()
{
	int a = 10;
	show(a);
	a = 20;
	cout << a << endl;
	system("pause");
	return 0;
}