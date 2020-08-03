//fun_temp.cpp

#include <iostream>

using namespace std;

template <typename T>
T add(T& a, T& b) {
	 return a + b;
}

void fun_temp_show() {
	float x = 3.1f, y = 4.33f;
	cout << add(x, y) << endl;
}