#include<iostream>
using namespace std;
//һά����
//��һ����ʽ�� �������� ������[���鳤��]     int arr[5]  
//�ڶ�����ʽ�� �������� ������[���鳤��]={}  int arr[5] ={1,2,3,4,5} 
//��������ʽ�� �������� ������[���鳤��]={}  int arr[ ] ={1,2,3,4,5} 
//int main()
//{
//	int arr[] = { 1,2,3,4,5 };
//	for (int i = 0; i < 5; i++)
//	{
//		cout << arr[i] << endl;
//	}
//	system("pause");
//	return 0;
//}

//һά����������;��1.����ͳ�������������ڴ��еĳ��� ��sizeof(arr)�� 2.���Ի�ȡ�������ڴ��е��׵�ַ
//int main()
//{
//	int arr[5] = { 1,2,3,4,5 };   //��������һ�������������Խ��и�ֵ����
//	cout << sizeof(arr) << endl;
//	cout << (int)arr << endl;
//	cout << &arr[0] << endl;
//	cout << sizeof(arr)/sizeof(arr[0]) << endl;
//	system("pause");
//	return 0;
//}

//���鵹��
//int main()
//{
//	int arr[5] = { 1,2,3,4,5};
//	int arr1[5];
//	int j = 0;
//	for (int i = sizeof(arr)/sizeof(arr[0])-1; i >= 0; i--,j++)
//	{
//		arr1[j] = arr[i];
//		
//	}
//	for (int x = 0; x < 5; x++)
//	{			
//		cout << arr1[x] << endl;
//	}
//	system("pause");
//	return 0;
//}
//int main()
//{
//	int arr[5] = { 1,2,3,4,5 };
//	int start = 0;
//	int end = sizeof(arr) / sizeof(arr[0])-1;
//	int temp = 0;
//	while (start < end)
//	{
//		temp = arr[start];
//		arr[start] = arr[end];
//		arr[end] = temp;
//		start++;
//		end--;
//	}
//	for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
//	{
//		cout << arr[i] << endl;
//	}
//	system("pause");
//	return 0;
//}

//ð������
//int main()
//{
//	int arr[6] = { 5,3,4,8,1,2 };
//	int temp = 0;
//	for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
//	{
//		for (int j = 0; j < sizeof(arr) / sizeof(arr[0]) - 1 - i; j++)
//		{
//			if (arr[j] > arr[j + 1])
//			{
//				temp = arr[j];
//				arr[j] = arr[j + 1];
//				arr[j + 1] = temp;
//			}
//		}
//
//	}
//	for (int i = 0; i < 6; i++)
//	{
//		cout << arr[i] << endl;
//	}
//	system("pause");
//	return 0;
//}

//��ά����1.�������ͣ�������[����][����]
        //2.�������ͣ�������[����][����] = {{}��{}}

//int main()
//{
//	int arr[2][5] = { {1,2,3,4,5},{6,7,8,9,10} };
//	for (int i = 0; i < 2; i++)
//	{
//		for (int j = 0; j < 5; j++)
//		{ 
//			cout << arr[i][j] << " ";
//		}
//		cout << endl;
//	}
//	system("pause");
//	return 0;
//}