//clazz.cpp

#include "clazz.h"
#include <string>

using namespace std;

struct Person {


	//����
	string name;
	int age;

	//Ĭ�Ϲ��캯��
	Person() {
		this->name = "liewei";
		this->age = 32;
	}

	//�Զ��幹�캯��
	Person(string name, int age) {
		this->name = name;
		this->age = age;
	}


	//����
	void say() {
		cout << "my name is " << this->name << ", I am " << this->age << " year old." << endl;
	}

	//��������
	~Person()
	{
		cout << "person �Ѿ����ͷ�" << endl;
	}
};

void clazz_show() {
	{
		Person liewei;
		liewei.age = 34;
		liewei.say();
	}
	cout << "----------------------" << endl;

	{
		Person* zhang = new Person("zhang3", 25);
		zhang->say();
		(*zhang).say();
	}
	cout << "**********************" << endl;
	
}
