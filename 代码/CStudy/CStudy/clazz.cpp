//clazz.cpp

#include "clazz.h"
#include <string>

using namespace std;

struct Person {


	//属性
	string name;
	int age;

	//默认构造函数
	Person() {
		this->name = "liewei";
		this->age = 32;
	}

	//自定义构造函数
	Person(string name, int age) {
		this->name = name;
		this->age = age;
	}


	//方法
	void say() {
		cout << "my name is " << this->name << ", I am " << this->age << " year old." << endl;
	}

	//析构函数
	~Person()
	{
		cout << "person 已经被释放" << endl;
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
