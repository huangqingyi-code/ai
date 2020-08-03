#include<iostream>
using namespace std;
//函数模板和类模板
//template <typename T>
//T add(T& a, T& b)
//{
//	return a + b;
//}
//int main()
//{
//	double a = 5.2, b = 3.2;
//	double c = add(a, b);
//	cout << c << endl;
//	system("pause");
//	return 0;
//}

template<class T>
class Person
{
public:
	T m_a;
	T m_b;
	Person(T a,T b):m_a(a),m_b(b){}
	T sum(){
		return m_a + m_b;
	}
};
int main()
{
	int a = 10, b = 20;
	Person<int>wusir(a,b);
	//int c = wusir.sum();
	cout << wusir.sum() << endl;
	system("pause");
	return 0;
}