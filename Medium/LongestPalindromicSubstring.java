package Medium;

public class LongestPalindromicSubstring {
    class Solution {
        public String longestPalindrome(String s) {
            String longest = "";
            String temp = "";
            String secondTemp = "";

            int left = 0;
            int right = 0;
            for(int i = 0; i < s.length(); i++) {
                temp = String.valueOf(s.charAt(i));
                left = i - 1;
                right = i + 1;
                while (left >= 0 && right < s.length()) {
                    if (s.charAt(left) != s.charAt(right)) {
                        break;
                    }
                    temp = String.valueOf(s.charAt(left)) + temp;
                    temp = temp + String.valueOf(s.charAt(right));
                    left--;
                    right++;
                }
                left = i - 1;
                right = i;
                if (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                    secondTemp = String.valueOf(s.charAt(left)) + String.valueOf(s.charAt(right));
                    left--;
                    right++;
                    while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                        secondTemp = String.valueOf(s.charAt(left)) + secondTemp + String.valueOf(s.charAt(right));
                        left--;
                        right++;
                    }
                }
                left = i;
                right = i + 1;
                if (left >= 0 && right < s.length() && s.charAt(right) == s.charAt(left)) {
                    secondTemp = String.valueOf(s.charAt(right)) + String.valueOf(s.charAt(left));
                    left--;
                    right++;
                    while (left >= 0 && right < s.length() && s.charAt(right) == s.charAt(left)) {
                        secondTemp = String.valueOf(s.charAt(left)) + secondTemp + String.valueOf(s.charAt(right));
                        left--;
                        right++;
                    }
                }
                if (temp.length() > longest.length()) {
                    longest = temp;
                }
                if (secondTemp.length() > longest.length()) {
                    longest = secondTemp;
                }
            }
            return longest;
        }
    }
}
