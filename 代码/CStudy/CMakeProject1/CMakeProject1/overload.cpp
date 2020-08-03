#include<iostream>
using namespace std;
class Person
{
public:
	int m_a;
	int m_b;
	Person(int a,int b):m_a(a),m_b(b){}
	/*Person operator+(const Person& p)
	{
		this->m_a += p.m_a;
		this->m_b += p.m_b;
		return *this;
	}*/
};
Person operator+(Person& p1, Person& p2)
{
	Person temp(0,0);
	temp.m_a = p1.m_a + p2.m_a;
	temp.m_b = p1.m_b + p2.m_b;
	return temp;

}
void test() {
	Person p1(10, 20);
	Person p2(30, 40);
	Person p3 = p1 + p2;
	cout << p3.m_a << endl;
	cout << p3.m_b << endl;
}
int main()
{
	test();
	system("pause");
	return 0;
}