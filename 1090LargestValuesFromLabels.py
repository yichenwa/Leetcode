class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        counts = collections.defaultdict(int)
        sortcom=sorted(zip(values,labels))#from least to most


        #countlabels=[]
        sum=0
        while num_wanted>0 and len(sortcom)>0:
            val,lab=sortcom.pop()
            if counts[lab]<use_limit:
                sum+=val
                counts[lab]+=1
                num_wanted-=1
        return sum
"""
#collections.defaultdict 建一个字典， int 是字典的类型，好处是就算key不存在也不会报错。在#20，如果counts【lab】不存在，就会新加一个lab

"""