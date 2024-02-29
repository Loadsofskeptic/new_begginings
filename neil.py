import sys
class Solution(object):
    def twoSum(self, nums, target):
        anormallist = {}
        counter = 0
        for i in range(len(nums)):
            if ((nums[i] == '[') or (nums[i] == ']') or (nums[i] == ',') or (int(target) < int(nums[i]))):
                counter += 1
                continue
            if (int(target) > int(nums[i])):
                valueminuser = i - counter
                anormallist[valueminuser] = nums[i]
                for v in range(len(anormallist)):
                    try:
                        if((int(anormallist[valueminuser]) + int(anormallist[v])) == int(target)):
                            self = [v, valueminuser]
                            print(self)
                            return self, nums, target
                    except (KeyError):
                        pass
            else: 
                return print("none was found")
    """
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    """
    pass


def main():
    random = Solution()
    printhere = random.twoSum(sys.argv[1], sys.argv[2])
    print("nums =", printhere)
    pass

if __name__ == "__main__":
    main()