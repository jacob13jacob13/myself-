#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Solution(object):
    def heapify(self,data,long,root):
            left=2*root+1#root的左邊元素
            right=2*root+2#root的右邊元素
            maxnumber=root-1#最大值
            #利用if,else找出root,long和root左右兩邊的元素
            if left<long and data[root]<=data[left]:
                maxnumber=left
            else:
                maxnumber=root
            if right<long and data[maxnumber]<=data[right]:
                maxnumber=right
            #若最大值不是root則進行交換    
            if maxnumber!=root:
                data[root],data[maxnumber]=data[maxnumber],data[root]
                self.heapify(data,long,maxnumber)                
    def heapsort(self,nums):
        long = len(nums)#判斷長度
        for root in range(long,-1,-1):#排序出最大的架構
            self.heapify(nums,long,root)
        for root in range(long-1,0,-1):#挑出元素
            nums[root],nums[0]=nums[0],nums[root]#進行交換
            self.heapify(nums,root,0)  
        return nums#執行


# In[ ]:




