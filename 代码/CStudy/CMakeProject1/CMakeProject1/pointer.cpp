#include<iostream>
using namespace std;

/*
int main()
{
	//1.定义指针
	int a = 10;
	//指针定义的语法：数据类型*指针变量名；
	int *p;
	//指针记录变量的地址
	p = &a;
	cout << "a的地址：" << p << endl;
	cout << sizeof(p) << endl;

	//2.使用指针    指针可以越界引用
	//可以通过解引用的方式来找到指针指向的内存；*p
	*p = 200;   //通过指针找到a的地址改变值
	cout << *p << endl;
	//指针占用内存：32位编译器占4个字节，64位编译器占8个字节（所有数据类型的指针都一样）
	float b = 32.5f;
	float *pit = &b;
	cout << sizeof(pit) << endl;
	system("pause");
	return 0;
}
*/

//空指针/野指针：指向非法的内存的空间，空指针和野指针都不是我们创建的不要去访问它
//int main()
//{
//	//指针变量p指向内存地址编号位0的空间
//	int *p = NULL;
//	//访问空指针报错
//	//内存0-255被系统占用内存，不允许用户访问
//	//*p = 10;   更改空指针指向的内存会报错
//	cout << p << endl;
//	int *prg = (int *)0x1100;
//	//cout << *prg << endl;  //不能解引用野指针指向的内存
//	system("pause");
//	return 0;
//}

//1.const修饰指针--常量指针。const int *p = &a，指针指向可以修改，指针指向的值不可以修改
//2.const修饰常量 --指针常量 。int *const p = &a，指针指向不可以修改，指向的值可以修改
//3.const既修饰指针又修饰常量， const int * const p = &a，都不可以修改
//int main()
//{
//	int a = 10;
//	int b = 20;
//	const int * p = &a;
//	*p = b;
//}

//数组和指针：利用指针访问数组中元素
//int main()
//{
//	double arr[5] = { 1.0,2.0,3.0,4.0,5.0 };  //arr是数组的首地址
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

//指针和函数,地址传递可以改变会改变实参，值传递不会修改实参
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

//冒泡排序
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
