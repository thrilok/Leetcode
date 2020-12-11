class Solution {
    public int maximumWealth(int[][] accounts) {
        int maximumWealth = 0;
        int customers = accounts[0].length;
        int banks = accounts.length;
        for (int i=0; i < banks; i++){
            int wealth = 0; 
            for (int j = 0; j <customers; j++){
                wealth += accounts[i][j];
            }
            if (wealth > maximumWealth) maximumWealth = wealth; 
        }
        return maximumWealth;
    }
}

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Richest Customer Wealth.
// Memory Usage: 38.8 MB, less than 44.10% of Java online submissions for Richest Customer Wealth.