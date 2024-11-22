def longestCommonPrefix(strs):
    common_prefix = ''
    for chars in zip(*strs):
        if all(characters == chars[0] for characters in chars):
            common_prefix += chars[0]
            return common_prefix

        else:
            return ''

print(longestCommonPrefix(['hell', 'hello', 'helmet']))
