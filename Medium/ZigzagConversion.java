package Medium;

public class ZigzagConversion {
    class Solution {
        public String convert(String s, int numRows) {
            String[] finalArr = new String[numRows];
            int size = 0;
            int index = 0;
            boolean isReverse = false;
            String finalString = "";

            Arrays.fill(finalArr,"");
            if(numRows == 1) return s;
            while(size < s.length()) {
                if(!isReverse) {
                    if(index >= numRows) {
                        index = index - 2;
                        isReverse = true;
                    } else {
                        finalArr[index] = finalArr[index] + String.valueOf(s.charAt(size));
                        index++;
                        size++;
                    }
                } else {
                    if(index < 0) {
                        index = index + 2;
                        isReverse = false;
                    } else {
                        finalArr[index] = finalArr[index] + String.valueOf(s.charAt(size));
                        index--;
                        size++;
                    }
                }
            }

            for(String curr : finalArr) {
                System.out.println(curr);
                finalString = finalString + curr;
            }
            return finalString;
        }
    }
}
