#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N; // ������ ���� �Է� �ޱ�

    string numbers;
    cin >> numbers; // ���ڵ� �Է� �ޱ�

    int sum = 0;
    for (int i = 0; i < N; ++i) {
        sum += numbers[i] - '0'; // �� �ڸ��� ���ڸ� ���ϱ�
    }

    cout << sum << endl; // ��� ���

    return 0;
}
