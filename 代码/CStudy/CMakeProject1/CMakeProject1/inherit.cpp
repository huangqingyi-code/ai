#include<iostream>
using namespace std;
//���м̳У�ԭ�ȹ��еĻ��ǹ��У������Ļ��Ǳ���
//�����̳У�ԭ�ȹ��еĺͱ����Ķ���ɱ���
//˽�м̳У�ԭ�ȹ��еĺͱ����ı��˽�е�

//�ڸ����зǾ�̬�ĳ�Ա���Զ��ᱻ�̳У�������˽�еĳ�Ա�ĳ�Ա���Ա������������˷��ʲ����������Ǳ��̳��ˡ�
//�̳��й����������˳�򣺼̳����ȵ��ø��๹�캯���ٵ������๹�캯�����ȵ������������ٵ��ø���������ջ���Ƚ������

//���������и�����ͬ���ĳ�Ա�ͺ���ʱ��Ĭ�ϵ������࣬Ҫ����ø����Ҫ��������Base::

//����̳ж����������μ̳���ѧ

//class Basepage
//{
//public:
//	void header() {
//		cout << "��ӭ��½" << endl;
//	}
//	void fooder() {
//		cout << "��������" << endl;
//	}
//	void left() {
//		cout << "������" << endl;
//	}
//};
//class Python :public Basepage
//{
//public:
//	void content() {
//		cout << "pthonѧ����Ƶ" << endl;
//	}
//};
//class Java :public Basepage
//{
//public:
//	void content() {
//		cout << "java��Ƶѧ��"<<endl;
//	}
//};
//void test() {
//	Python p;
//	p.header();
//	p.fooder();
//	p.left();
//	p.content();
//	Java j;
//	j.header();
//	j.fooder();
//	j.left();
//	j.content();
//}
//int main() {
//	test();
//	system("pause");
//	return 0;
//}

class Base
{
public:
	int m_a;
	Base()
	{
		m_a = 100;
	}
	void func() {
		cout << "base func()" << endl;
	}
};
class Son :public Base
{
public:
	int m_a;
	Son()
	{
		m_a = 200;
	}
	void func()
	{
		cout << "son func()" << endl;
	}
};
int c = 6;
int main()
{
	Son s;
	cout << s.m_a << endl;
	cout << s.Base::m_a << endl;
	system("pause");
	return 0;
}