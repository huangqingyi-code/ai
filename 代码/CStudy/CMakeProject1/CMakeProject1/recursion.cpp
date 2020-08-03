// CMakeProject1.cpp: 定义应用程序的入口点。
//

#include "CMakeProject1.h"

using namespace std;
//
//int main()
//{
//	int i = 0;
//	do
//	{
//		cout << i << endl;
//		i++;
//	} while (i < 10);
//	system("pause");
//	return 0;
//}
//int main()
//{
//	int i = 0;
//	while (i < 10)
//	{
//		cout << i << endl;
//		i++;
//	}
//	system("pause");
//	return 0;
//}
//int main()
//{
//	int score = 0;
//	cout << "please input your score" << endl;
//	cin >> score;
//	if (score > 600)
//	{
//		if (score > 700)
//		{
//			cout << "考上了清华" << endl;
//		}
//		else if (score > 650)
//		{
//			cout << "考上了厦大" << endl;
//
//		}
//		else
//		{
//			cout << "考上了太原理工" << endl;
//		}
//	}
//	else if (score > 500)
//	{
//		cout << "考上了二本" << endl;
//	}
//	else
//	{
//		cout << "考上了三本" << endl;
//
//	}
//	system("pause");
//	return 0;
//}
//int main()
//{
//	int num = rand() % 100 + 1;  //rand()%100 随机生成0-99的随机数
//	//cout << num << endl;
//	int val = 0;
//	while (1)
//	{
//		cout << "please input a number" << endl;
//		cin >> val;
//		if (val > num)
//		{
//			cout << "it is too big" << endl;
//		}
//		else if (val < num)
//		{
//			cout << "it is too small" << endl;
//		}
//		else
//		{
//			cout << "congratulation" << endl;
//			break;
//		}
//	}
//	system("pause");
//	return 0;
//}

//int main()
//{
//	int num = 100;
//	int a = 0;  
//	int b = 0;
//	int c = 0;
//	while (num < 1000)
//	{
//		a = num % 10;  //个位数
//		b = num / 10 % 10;  //十位数
//		c = num / 100;  //百位数
//		cout << a << b<<c<<endl;
//		if (a*a*a+b*b*b+c*c*c==num)
//		{
//			cout << num << endl;
//		}
//		num++;
//	}
//	system("pause");
//	return 0;
//}
//
//int main()
//{
//	for (int i = 1; i < 101; i++)
//	{
//		int a = 0;
//		int b = 0;
//		int c = 0;
//		a = i % 10;
//		b = i / 10;
//		c = i % 7;
//		if (a == 7 || b == 7||c ==0)
//		{
//			cout << "敲桌子" << endl;
//		}
//		else
//		{
//			cout << i << endl;
//		}
//	}
//	system("pause");
//	return 0;
//}
//int main()
//{
//	for (int i = 1; i < 10; i++)
//	{
//		int j = 0;
//		j = i ;
//		while (j < 10)
//		{
//			int num = 0;
//			num = i * j;
//			cout << i << " * " << j <<" = "<< num << endl;
//			j++;
//		}
//	}
//	system("pause");
//	return 0;
//}

int main()
{
	int i = 0;
	do
	{
		i++;
		cout << i << endl;
	} while (i < 1);
	system("pause");
	return 0;
}