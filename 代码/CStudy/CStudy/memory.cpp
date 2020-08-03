//memory.cpp
//

#include "memory.h"
#include <Windows.h>

using namespace std;

//栈中变量的错误使用演示
void stack() {
	int* ptr_a = NULL;
	{
		int a = 3;//栈中声明一个变量a,当执行出作用域后，变量会被自动清理
		ptr_a = &a;
		cout << *ptr_a << endl;
	}
	cout << *ptr_a << endl; //这是错误的，因为这时候a已经被释放。
}

//堆
void heap() {
	int* ptr_a = NULL;
	{
		//在堆中声明一个变量，初始化值为3，并把该变量的指针传递给ptr_a指针变量
		ptr_a = new int(4);
	}
	cout << *ptr_a << endl; //这不会有任何问题

	delete ptr_a; // 如果不执行这句，内存会泄露
}

//泄露
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
