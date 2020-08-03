//inherit.cpp

#include "inherit.h"
#include <string>

using namespace std;

class Animal {

protected:
	string m_sex;//����ĸ


public:
	//���캯������ð�ų�ʼ����Ա����
	//classĬ����˽�У����캯�������ڹ������򣬷����޷�ʵ����
	Animal(string sex) :m_sex(sex) {}

	//����һ�����鷽��
	//virtual void say() = 0;

	//����һ���鷽��
	virtual void say() {
		cout << "What is the sex of the Animal ?" << endl;
	}

	//����һ����ͨ����
	/*void say() {
		cout << "What is the sex of the Animal ?" << endl;
	}*/

};

class Cat :public Animal {

public:
	Cat(string sex) :Animal(sex) {}

	void say() {
		cout << "This cat's sex is " << this->m_sex << "." << endl;
	}
};

void inherit_show() {
	//Cat* mycat = new Cat("��");
	Animal* mycat = new Cat("��");
	mycat->say();
	delete mycat;

}
