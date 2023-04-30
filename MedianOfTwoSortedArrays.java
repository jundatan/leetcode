public class MedianOfTwoSortedArrays {
    class Solution {
        public double findMedianSortedArrays(int[] nums1, int[] nums2) {
            int[] temp = new int[nums1.length + nums2.length];

            for(int i = 0; i < nums1.length; i++) {
                temp[i] = nums1[i];
            }
            for(int i = nums1.length; i < temp.length; i++) {
                temp[i] = nums2[i - nums1.length];
            }
            Arrays.sort(temp);
            System.out.println(Arrays.toString(temp));

            if(temp.length % 2 == 0) {
                return (double) (temp[temp.length/2] + temp[temp.length/2 - 1]) / 2;
            } else {
                return temp[temp.length/2];
            }
        }
    }
}
