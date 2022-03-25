class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list[int])-> TreeNode:
    def helper (l, r):
        if l > r: 
            return None
        
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = helper(l,mid-1)
        root.right = helper(mid+1, r)
        return root
    return helper(0,len(nums)-1)

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(sortedArrayToBST(nums))
