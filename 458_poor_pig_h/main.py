class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        rounds = minutesToTest / minutesToDie
        return int(math.ceil(math.log(buckets, rounds + 1)))
    
# I figure out when min_die == min_test
# buckets can be thought of n-cube with edge equal 2
# We need n pigs to test it. So log(buckets, 2)

# To generalize, if min_test / min_die = r, than it will be the r + 1 cube