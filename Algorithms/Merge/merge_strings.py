class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged_string = []

        len1, len2 = len(word1), len(word2)
        print(f'\nLength of word1: {len1}, word2: {len2}')

        max_len = max(len1, len2)
        print(f'Max length: {max_len}\n')

        for i in range(max_len):
            if i < len1:
                print(f'{merged_string} - {word1[i]} - iteration --> {i} - {len1} - {len2}')
                merged_string.append(word1[i])
                print(f'{merged_string} - {word1[i]} - iteration --> {i} - {len1} - {len2}')
            if i < len2:
                print(f'{merged_string} - {word2[i]} - iteration --> {i} - {len1} - {len2}')
                merged_string.append(word2[i])
                print(f'{merged_string} - {word2[i]} - iteration --> {i} - {len1} - {len2}')

        return ''.join(f'\nMerged String [Final] : {merged_string}')


merge = Solution().mergeAlternately("abc", "pqrst")
print(merge)