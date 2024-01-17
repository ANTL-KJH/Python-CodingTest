#include <iostream>
using namespace std;

#define MAX 1000001
bool arr[MAX];
int main(void)
{
	int T;
	cin >> T;
	for (int i = 0; i < MAX; i++)
	{
		arr[i] = true;
	}
	arr[0] = arr[1] = false;
	for (int i = 2; i * i < MAX; i++)
	{
		if (arr[i])
		{
			for (int j = i * 2; j < MAX; j += i)
				arr[j] = false;
		}
	}
	for (int i = 0; i < T; i++)
	{
		int testNum, count=0;
		cin >> testNum;
		for (int p = 2; p <= testNum / 2; p++)
			if ((arr[p] & arr[testNum - p]) == true)
				count++;
		cout << count <<"\n";
	}
	return 0;
}