#include<iostream>
using namespace std;
#include <windows.h>
//内存分区模型：
//1.代码区：存放函数体的二进制代码，由操作系统管理/特点：共享的，频繁执行时只开辟一个内存；只读的
//2.全局区：放全局变量和静态变量以及常量
//3.栈区：由编译器自动分配释放，存放函数的形参，局部变量等
//4.堆区：由程序员分配和释放，若程序员不释放，程序结束时操作系统回收，
//意义：不同区域存放的数据，赋予不同的生命周期，给我们更大的灵活编程

//在程序编译后生成.exe的可执行程序，未执行的程序前分为：代码区和全局区
//代码区：存放CPU可执行的机器指令，特点：共享的，频繁执行时只开辟一个内存；只读的
//全局区：全局变量和静态变量以及常量，该区域的数据程序结束后操作系统释放
/*
int g_a = 10;  //全局变量
int main()
{
	//创建普通局部变量
	int a = 10;
	int b = 20;
	cout << "局部变量a的地址" << (int)&a << endl;
	cout << "局部变量b的地址" << (int)&b << endl;
	cout << "全局变量的g_a的地址" << (int)&g_a << endl;
	//静态变量
	static int s_a = 10;
	cout << "静态变量的s_a的地址" << (int)&s_a << endl;
	//常量：1.字符串常量 2.const修饰常量（const修饰的局部常量不在全局区）
	system("pause");
	return 0;
}
*/

//程序运行后
//栈区：由编译器自动分配释放，存放函数的参数值，局部变量等
//注意事项：不用返回局部变量的地址；栈区开辟的空间由编译器自动释放，函数结束时这个内存空间被清空

//堆区：由程序员分配和释放，若程序员不释放，程序结束时操作系统回收
//c++中主要利用new在堆区开辟内存
//int * func()
//{
//	//int a = 30;
//	//int * p = &a;
//	int *p = new int(10);
//	return p;
//}
//int main()
//{
//	int *p = func();
//	//cout << *p << endl; //func()，return的值清空了，要用new
//	cout << *p << endl; //func()
//	system("pause");
//	return 0;
//}

//new操作   new前面必须是一个指针
//void print(int *arr)
//{
//	for (int i = 0; i < 10; i++)
//	{
//		cout << arr[i] << endl;
//	}
//}
//void func()
//{
//	int *arr = new int[10];
//	for (int i = 0; i < 10; i++)
//	{
//		arr[i] = i + 10;
//	}
//	print(arr);
//	delete[] arr;
//}
//int main()
//{
//	func();
//	int arr1[2] = { 1,2 };
//	cout << *arr1 << endl;
//	system("pause");
//	return 0;
//}

void func()
{
	//int *arg = new int[10];
	for (int i = 0; i < 10000; i++)
	{
		int *arg = new int[1000000];
		Sleep(1);
	}
	//delete[] arg;
}
int main()
{
	int *par = new int(10);
	func();
	system("pause");
	return 0;

}