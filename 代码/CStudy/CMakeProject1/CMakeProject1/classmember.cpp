#include<iostream>
using namespace std;
#include<string>

//�������Ϊ���Աʱ�������������Ϊ����ĳ�Աʱ���ȹ��촫����࣬�ٹ������������෴
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