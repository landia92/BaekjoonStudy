#include <iostream>
#include <climits>

using namespace std;

int main() {
    int N;
    cin >> N; // ������ ���� �Է� �ޱ�

    int min_val = INT_MAX; // �ּڰ��� ������ ����, �ʱⰪ�� INT_MAX�� ����
    int max_val = INT_MIN; // �ִ��� ������ ����, �ʱⰪ�� INT_MIN���� ����

    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num; // ���� �Է� �ޱ�

        // ���� �Էµ� ���� �ּڰ����� ������ �ּڰ��� ����
        if (num < min_val) {
            min_val = num;
        }

        // ���� �Էµ� ���� �ִ񰪺��� ũ�� �ִ��� ����
        if (num > max_val) {
            max_val = num;
        }
    }

    cout << min_val << " " << max_val << endl; // �ּڰ��� �ִ� ���

    return 0;
}
