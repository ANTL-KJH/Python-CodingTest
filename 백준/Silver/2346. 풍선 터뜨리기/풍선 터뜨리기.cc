#include <iostream>
#include <deque>
using namespace std;

deque<pair<int, int>> dq;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N;
	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		int value;
		cin >> value;
		dq.push_back({ value,i });
	}

	while (true)
	{
		cout << dq.front().second << " ";
		int frt = abs(dq.front().first);
		int ff = dq.front().first;
		dq.pop_front();

		if (dq.empty()) break;

		if (ff<0)
		{
			for (int i = 0; i < frt; i++)
			{
				dq.push_front(dq.back());
				dq.pop_back();
			}
		}
		else
		{
			for (int i = 0; i < frt - 1; i++)
			{
				dq.push_back(dq.front());
				dq.pop_front();
			}
		}
	}

	return 0;
}