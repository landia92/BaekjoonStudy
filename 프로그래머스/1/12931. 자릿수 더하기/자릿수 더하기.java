import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        String s = Integer.toString(n);
        for(int i = 0; i<s.length(); i++){
            answer = answer + (int)s.charAt(i) - 48;
        }

        return answer;
    }
}