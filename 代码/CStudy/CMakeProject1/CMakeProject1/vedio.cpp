#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;

//ָ�����飺���Ǹ�����
//��ֵָ�룺ָ��
//int main()
//{
//	int a[] = { 1,2,3 };
//	int* p[3];
//	p[0] = &a[0];
//	p[1] = &a[1];
//	p[2] = &a[2];
//	cout << &p[0] << endl;
//	cout << p << endl;
//	system("pause");
//	return 0;
//}

//�ַ�ָ��
//int main() {
//	char str[] = "hello";
//	char *p = str;
//	cout << *(str+1) << endl;
//	system("pause");
//	return 0;
//}

int main() {
	string str = "hello";
	string *p = &str;
	cout << *(p) << endl;
	system("pause");
	return 0;
}