#include<iostream>
using namespace std;
#include<string>
//����Ȩ�ޣ�����Ȩ��public��Ա���ڿ��Է��ʣ�������Է���
          //����Ȩ��protected ���ڿ��Է��ʣ����ⲻ���ԣ��̳�ʱ������Է���
          //˽��Ȩ��private   ���ڿ��Է��ʣ����ⲻ���ԣ��̳�ʱ���಻���Է��� 
          //Ĭ��˽��
// struct Ĭ��Ȩ�޹���  classĬ��˽��

//const double PI = 3.14;
//class Circle
//{
//public:
//	int r;
//	double ciculate()
//	{
//		return 2 * PI*r;
//	}
//
//};
//int main()
//{
//	Circle c;
//	c.r = 10;
//	cout << c.ciculate() << endl;
//	system("pause");
//	return 0;
//}

//class Student
//{
//public:
//	string name;
//	int number;
//	void show()
//	{
//		cout << "name:" << name << "number:" << number << endl;
//	}
//};
//int main()
//{
//	Student alex;
//	alex.name = "alex";
//	alex.number = 10;
//	alex.show();
//	system("pause");
//	return 0;
//}


//��Ա��������λ˽�У�1.�����Լ����ƶ�д����2.����д���Լ�����ݵ���Ч��
//class Person
//{
//private:
//	string name;
//	int age;
//	int passward;
//public:
//	void set_name(string name0)
//	{
//		name = name0;
//	}
//	void set_age(int age0)
//	{
//		if (age0 < 0 || age0>100)
//		{
//			cout << "out of range" << endl;
//		}
//		else
//		{
//			age = age0;
//		}
//	}
//	void get_psw()
//	{
//		passward = 123456;
//		cout << passward << endl;
//		
//	}
//};
//int main()
//{
//	Person wusir;
//	wusir.set_age(120);
//	wusir.get_psw();
//	system("pause");
//	return 0;
//}

//class Cube
//{
//private:
//	int m_l;
//	int m_w;
//	int m_h;
//public:
//	void make_l(int l)
//	{
//		m_l = l;
//	}
//	int get_l()
//	{
//		return m_l;
//	}
//	void make_w(int w)
//	{
//		m_w = w;
//	}
//	int get_w()
//	{
//		return m_w;
//	}
//	void make_h(int h)
//	{
//		m_h = h;
//	}
//	int get_h()
//	{
//		return m_h;
//	}
//	int area()
//	{
//		return m_l * m_w*m_h;
//	}
//	void issamebyclass(Cube &c)
//	{
//		if (m_l == c.get_l() && m_h == c.get_h() && m_w == c.get_w())
//		{
//			cout << "same"<< endl;
//		}
//		else
//		{
//			cout << "different" << endl;
//		}
//
//	}
//
//};
//bool issame(Cube &c1, Cube &c2)
//{
//	if (c1.get_h() == c2.get_h() && c1.get_l() == c2.get_l() && c1.get_w() == c2.get_w())
//	{
//		return true;
//	}
//	else
//	{
//		return false;
//	}
//}
//int main()
//{
//	Cube c1;
//	c1.make_l(10);
//	c1.make_w(10);
//	c1.make_h(10);
//	Cube c2;
//	c2.make_l(10);
//	c2.make_w(10);
//	c2.make_h(10);
//	c1.issamebyclass(c2);
//	/*bool ret = issame(c1, c2);
//	if (ret)
//	{
//		cout << "same" << endl;
//	}
//	else
//	{
//		cout << "different" << endl;
//	}*/
//	cout << c1.area() << "  " << c2.area()<<endl;
//	system("pause");
//	return 0;
//}