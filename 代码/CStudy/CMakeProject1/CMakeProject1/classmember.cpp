#include<iostream>
using namespace std;
#include<string>

//类对象作为类成员时，其他类对象作为本类的成员时，先构造传入的类，再构造自身，析构相反
class Phone
{
public:
	string pname;
	Phone(string name):pname(name){}
};
class Person
{
public:
	string mname;
	Phone mphone;
	Person(string name,string phname):mname(name),mphone(phname){}
};
int main()
{
	Person wusir("wusir", "huawei mate20");
	cout << wusir.mphone.pname <<endl;
	system("pause");
	return 0;
}