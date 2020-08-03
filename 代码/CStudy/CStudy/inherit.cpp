//inherit.cpp

#include "inherit.h"
#include <string>

using namespace std;

class Animal {

protected:
	string m_sex;//公或母


public:
	//构造函数，用冒号初始化成员变量
	//class默认是私有，构造函数必须在公共区域，否则无法实例化
	Animal(string sex) :m_sex(sex) {}

	//定义一个纯虚方法
	//virtual void say() = 0;

	//定义一个虚方法
	virtual void say() {
		cout << "What is the sex of the Animal ?" << endl;
	}

	//定义一个普通方法
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
	//Cat* mycat = new Cat("公");
	Animal* mycat = new Cat("公");
	mycat->say();
	delete mycat;

}
