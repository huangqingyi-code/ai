//ref.cpp
//

#include "ref.h"

using namespace std;

void ref_show() {
	// �����򵥵ı���
	int    i=3;
	double d=4;

	// �������ñ���
	int&    r = i;
	double& s = d;

	i = 5;
	cout << "Value of i : " << i << endl;
	cout << "Value of i reference : " << r << endl;

	d = 11.7;
	cout << "Value of d : " << d << endl;
	cout << "Value of d reference : " << s << endl;
}
