#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T; // �׽�Ʈ ���̽��� ���� �Է� �ޱ�

    for (int t = 0; t < T; ++t) {
        int R;
        string S;
        cin >> R >> S; // �ݺ� Ƚ�� R�� ���ڿ� S �Է� �ޱ�

        for (char c : S) {
            for (int i = 0; i < R; ++i) {
                cout << c; // ���ڸ� R�� �ݺ��Ͽ� ���
            }
        }

        cout << endl; // �׽�Ʈ ���̽��� ��� ��� �� ����
    }

    return 0;
}
