//loop.cpp
//

#include "loop.h"

using namespace std;

//forѭ��
void for_loop() {
	int a[] = { 1,2,3,4,5,6 };
	for (int i = 0; i < 6; i++) {
		cout << a[i] << endl;
	}
}

//foreachѭ��
void foreach_loop() {
	int a[] = { 1,2,3,4,5,6 };
	for (int& k : a) {
		cout << k << endl;
	}
}

//whileѭ��
void while_loop() {
	int a[] = { 1,2,3,4,5,6 };
	int i = 0;
	while (i < 6) {
		cout << a[i++] << endl;
	}
}

//do...whileѭ��
void do_while_loop() {
	int a[] = { 1,2,3,4,5,6 };
	int i = 0;
	do {
		cout << a[i++] << endl;
	} while (i < 6);
}

void loop_show() {
	//for_loop();
	//foreach_loop();
	//while_loop();
	do_while_loop();
}
