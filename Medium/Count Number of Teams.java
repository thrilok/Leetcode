class Solution {
    public int numTeams(int[] rating) {
        int len = rating.length;
        if (len <3) return 0;
        int count = 0;
        int currentIndex = 1;
        while (currentIndex < len-1){
            int pre_les = 0;
        int pre_gre = 0;
        int nex_les = 0;
        int nex_gre = 0;
            for (int index= 0; index <len; index++) {
                if (index != currentIndex){
                    int currentVal = rating[currentIndex];
                if ((index<currentIndex) && ( rating[index] < currentVal)) pre_les+=1; 
                else if ((index<currentIndex) && (rating[index] > currentVal))  pre_gre +=1;
                else if ((index>currentIndex) && (rating[index] < currentVal)) nex_les+=1;
                else if ((index>currentIndex) && (rating[index] > currentVal))  nex_gre +=1;
                }
            }
            count += (pre_les*nex_gre) + (pre_gre*nex_les);
            currentIndex +=1;
        }
        return count;
    }
}

// Runtime: 3 ms, faster than 67.04% of Java online submissions for Count Number of Teams.
// Memory Usage: 36.6 MB, less than 38.82% of Java online submissions for Count Number of Teams.