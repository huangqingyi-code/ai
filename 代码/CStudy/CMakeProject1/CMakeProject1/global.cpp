#include<iostream>
#include<string>
using namespace std;

int a = 3;
int b; //全局变量可以不赋值，系统默认赋值0

int main()
{
	int c;
	cout << &c << endl;
	cout << ::b << endl;   //打印全局变量
	{
		int d = 6;
	}
	//cout << d << endl;  外面不能调用里面的，里面的可以调用外面的
	system("pause");
	return 0;
}