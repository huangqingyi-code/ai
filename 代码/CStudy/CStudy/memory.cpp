//memory.cpp
//

#include "memory.h"
#include <Windows.h>

using namespace std;

//ջ�б����Ĵ���ʹ����ʾ
void stack() {
	int* ptr_a = NULL;
	{
		int a = 3;//ջ������һ������a,��ִ�г�������󣬱����ᱻ�Զ�����
		ptr_a = &a;
		cout << *ptr_a << endl;
	}
	cout << *ptr_a << endl; //���Ǵ���ģ���Ϊ��ʱ��a�Ѿ����ͷš�
}

//��
void heap() {
	int* ptr_a = NULL;
	{
		//�ڶ�������һ����������ʼ��ֵΪ3�����Ѹñ�����ָ�봫�ݸ�ptr_aָ�����
		ptr_a = new int(4);
	}
	cout << *ptr_a << endl; //�ⲻ�����κ�����

	delete ptr_a; // �����ִ����䣬�ڴ��й¶
}

//й¶
void leak() {
	for (int i = 1; i < 1000000; i++) {
		int* a = new int[100000];
		//int a[100000];
		//delete[] a;
		Sleep(1);
	}
}

void memory_show() {

	//stack();
	//heap();
	leak();


}
