#include<iostream>
using namespace std;

/*
int main()
{
	//1.����ָ��
	int a = 10;
	//ָ�붨����﷨����������*ָ���������
	int *p;
	//ָ���¼�����ĵ�ַ
	p = &a;
	cout << "a�ĵ�ַ��" << p << endl;
	cout << sizeof(p) << endl;

	//2.ʹ��ָ��    ָ�����Խ������
	//����ͨ�������õķ�ʽ���ҵ�ָ��ָ����ڴ棻*p
	*p = 200;   //ͨ��ָ���ҵ�a�ĵ�ַ�ı�ֵ
	cout << *p << endl;
	//ָ��ռ���ڴ棺32λ������ռ4���ֽڣ�64λ������ռ8���ֽڣ������������͵�ָ�붼һ����
	float b = 32.5f;
	float *pit = &b;
	cout << sizeof(pit) << endl;
	system("pause");
	return 0;
}
*/

//��ָ��/Ұָ�룺ָ��Ƿ����ڴ�Ŀռ䣬��ָ���Ұָ�붼�������Ǵ����Ĳ�Ҫȥ������
//int main()
//{
//	//ָ�����pָ���ڴ��ַ���λ0�Ŀռ�
//	int *p = NULL;
//	//���ʿ�ָ�뱨��
//	//�ڴ�0-255��ϵͳռ���ڴ棬�������û�����
//	//*p = 10;   ���Ŀ�ָ��ָ����ڴ�ᱨ��
//	cout << p << endl;
//	int *prg = (int *)0x1100;
//	//cout << *prg << endl;  //���ܽ�����Ұָ��ָ����ڴ�
//	system("pause");
//	return 0;
//}

//1.const����ָ��--����ָ�롣const int *p = &a��ָ��ָ������޸ģ�ָ��ָ���ֵ�������޸�
//2.const���γ��� --ָ�볣�� ��int *const p = &a��ָ��ָ�򲻿����޸ģ�ָ���ֵ�����޸�
//3.const������ָ�������γ����� const int * const p = &a�����������޸�
//int main()
//{
//	int a = 10;
//	int b = 20;
//	const int * p = &a;
//	*p = b;
//}

//�����ָ�룺����ָ�����������Ԫ��
//int main()
//{
//	double arr[5] = { 1.0,2.0,3.0,4.0,5.0 };  //arr��������׵�ַ
//	double *p = arr;
//	//cout << *p << endl;
//	for (int i = 0; i < 5; i++)
//	{
//		cout << *p << endl;
//		p++;
//	}
//	system("pause");
//	return 0;
//}

//ָ��ͺ���,��ַ���ݿ��Ըı��ı�ʵ�Σ�ֵ���ݲ����޸�ʵ��
//void swap(int *p1,int *p2)
//{
//	int temp = *p1;
//	*p1 = *p2;
//	*p2 = temp;
//}
//int main()
//{
//	int a = 10;
//	int b = 20;
//	swap(&a,&b);
//	cout << a << b << endl;
//	system("pause");
//	return 0;
//}

//ð������
/*
void bubblesort(int *arr, int len)
{
	for (int i = 0; i < len; i++)
	{
		for (int j = 0; j < len - i - 1; j++)
			if (arr[j] > arr[j + 1])
			{
				int temp = 0;
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
	}
}
int main()
{
	int arr[8] = { 2,5,3,9,1,6,10,4 };
	int len = sizeof(arr) / sizeof(arr[0]);
	bubblesort(arr, len);
	for (int i = 0; i < len; i++)
	{
		cout << arr[i] << endl;
	}
	system("pause");
	return 0;
}
*/
