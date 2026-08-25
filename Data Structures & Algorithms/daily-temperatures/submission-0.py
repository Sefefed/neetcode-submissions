class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st = [0]
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] < temperatures[st[-1]]:
                st.append(i)
            while st and temperatures[i] > temperatures[st[-1]]:
                ind = st.pop() 
                ans[ind] = i - ind
            st.append(i) 
        return ans      
             