#include<iostream>
using namespace std;
//int add(int num1, int num2)
//{
//	int sum = num1 + num2;
//	return sum;
//}
//int main()
//{
//	int a = 10;
//	int b = 20;
//	int sum = add(a, b);
//	cout << sum << endl;
//	system("pause");
//	return 0;
//}

//void swap(int num1, int num2)  //void当不需要返回值时用void
//{
//	cout << "交换前的数据" << num1 << " " <<num2 << endl;
//	int temp = num1;
//	num1 = num2;
//	num2 = temp;
//	cout << "交换后的数据" << num1 << " " << num2 << endl;
//}
//int main()
//{
//	int a = 10;
//	int b = 20;
//	swap(a, b);      //交换前后并不会影响a,b的值，值传递时，形参是修饰不了实参的
//	system("pause");
//	return 0;
//}

//函数声明
//int max(int a, int b);  //函数再main函数下面，要执行的话要先声明
//
//int main()
//{
//	int res = max(5, 9);
//	cout << res << endl;
//	system("pause");
//	return 0;
//}
//
//int max(int a, int b)
//{
//	return a > b ? a : b;
//}